
from pydantic import BaseModel


class UserLikeModel(BaseModel):
    user_name: str

    class Config:
        orm_mode = True
        cache_ok = True
        arbitrary_types_allowed = True
