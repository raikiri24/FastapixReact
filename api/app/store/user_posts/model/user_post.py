from typing import Optional
from pydantic import BaseModel


class ListUserPost(BaseModel):
    id: int
    title: str
    description: Optional[str]
    likes_count: Optional[int]

    class Config:
        orm_mode = True
        cache_ok = True
        arbitrary_types_allowed = True


class UserPost(BaseModel):
    id: int
    title: str
    description: Optional[str]
    likes_count: Optional[int]

    class Config:
        orm_mode = True
        cache_ok = True
        arbitrary_types_allowed = True


class UserPostCreate(BaseModel):
    title: str
    description: Optional[str]
    owner_id: int

    class Config:
        orm_mode = True
        cache_ok = True
        arbitrary_types_allowed = True
