from app.service.database.database import Base
from sqlalchemy import Boolean, Column, Integer, String, Numeric
from sqlalchemy.orm import relationship
from typing import ClassVar
from datetime import time
from app.store.user_posts.schema.user_post import Posts
from app.store.post_likes.schema.post_likes import Likes


class UserProfile(Base):
    __tablename__ = "users"
    LABEL: ClassVar[str] = 'Users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), unique=True, index=True)
    user_name = Column(String(50), unique=True, index=True)
    first_name = Column(String(50))
    middle_name = Column(String(50))
    last_name = Column(String(50))
    password = Column(String(20))
    birthday = Column(Numeric(precision=20, scale=7), nullable=True)
    address = Column(String(100), nullable=True)
    is_active = Column(Boolean, default=True)
    phone_number = Column(String(30), nullable=True)
    posts = relationship(Posts, backref="users.id", lazy='selectin')
    likes = relationship(Likes, backref="users.id", lazy='selectin')
    created_at = Column(Numeric(precision=20, scale=7), default=time())
    updated_at = Column(Numeric(precision=20, scale=7), default=time())
    deleted_at = Column(Numeric(precision=20, scale=7), nullable=True)
