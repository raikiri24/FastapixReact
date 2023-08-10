from typing import List, Optional
from pydantic import BaseModel
from app.store.user_profile.model.user_likers import UserLikeModel


class Likes(BaseModel):

    user: Optional[List[UserLikeModel]]

    class Config:
        orm_mode = True
        cache_ok = True
        arbitrary_types_allowed = True
