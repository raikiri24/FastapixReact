from app.store.user_posts.model.user_post import UserPost
from pydantic import BaseModel
from typing import Optional
from typing import List


class UserProfile(BaseModel):

    user_name: str
    email: Optional[str]
    first_name: str
    middle_name: Optional[str]
    last_name: str
    password: str
    birthday: Optional[float]
    address: Optional[str]
    is_active: Optional[bool]
    phone_number: Optional[str]
    created_at: float
    updated_at: float
    deleted_at: Optional[float]
    posts: Optional[List[UserPost]]

    class Config:
        orm_mode = True
        cache_ok = True
        arbitrary_types_allowed = True


class UserProfileForPost(BaseModel):

    user_name: str
    email: Optional[str]
    first_name: str
    middle_name: Optional[str]
    last_name: str
    password: str
    is_active: Optional[bool]

    class Config:
        orm_mode = True
        cache_ok = True
        arbitrary_types_allowed = True


class UserProfileCreate(BaseModel):
    user_name: str
    email: Optional[str]
    first_name: str
    middle_name: Optional[str]
    last_name: str
    password: str
    birthday: Optional[float]
    address: Optional[str]
    is_active: Optional[bool]
    phone_number: Optional[str]

    class Config:
        orm_mode = True
        cache_ok = True
        arbitrary_types_allowed = True


class UserProfileUpdateModel(BaseModel):
    user_name: Optional[str]
    email: Optional[str]
    first_name: Optional[str]
    middle_name: Optional[str]
    last_name: Optional[str]
    password: Optional[str]
    birthday: Optional[str]
    address: Optional[str]
    updated_at: Optional[float]
    deleted_at: Optional[float]
