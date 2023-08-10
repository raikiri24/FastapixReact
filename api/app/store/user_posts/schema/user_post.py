from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, select, func
from sqlalchemy.orm import relationship, mapped_column, column_property
from app.store.post_likes.schema.post_likes import Likes
from app.service.database.database import Base
from datetime import time


class Posts(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(String(255))
    owner_id = mapped_column(Integer, ForeignKey("users.id"))
    owner = relationship("UserProfile", back_populates="posts",
                         lazy='joined', overlaps='owner')
    likes = relationship(Likes, backref="posts.id", lazy='selectin')
    likes_count = column_property(
        select(func.count(Likes.id))
        .where(Likes.post_id == id)
        .correlate_except(Likes)
        .scalar_subquery()
    )
    created_at = Column(Numeric(precision=20, scale=7), default=time())
    updated_at = Column(Numeric(precision=20, scale=7), default=time())
    deleted_at = Column(Numeric(precision=20, scale=7), nullable=True)
