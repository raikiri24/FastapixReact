from app.service.database.database import Base
from sqlalchemy import Column, Integer, ForeignKey

from sqlalchemy.orm import mapped_column


class Likes(Base):
    __tablename__ = "likes"
    id = Column(Integer, primary_key=True)
    post_id = mapped_column(Integer, ForeignKey("posts.id"))
    user_id = mapped_column(Integer, ForeignKey("users.id"))
