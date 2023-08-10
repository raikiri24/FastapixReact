from typing import Optional
from pydantic import BaseModel
from app.store.user_profile.model.user_profile import UserProfileForPost


class GetUserPost(BaseModel):
    id: int
    title: str
    description: Optional[str]
    likes_count: Optional[int]
    owner: Optional[UserProfileForPost]

    class Config:
        orm_mode = True
        cache_ok = True
        arbitrary_types_allowed = True
