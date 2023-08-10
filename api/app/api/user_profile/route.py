from app.store.user_profile.model.user_profile import UserProfile, UserProfileUpdateModel, UserProfileCreate
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from app.service.database.database import get_db
from app.api.user_profile import controller
from fastapi import APIRouter, Depends
from typing import Optional


router = APIRouter(
    prefix="/api/user-profile",
)


@router.get("/{user_profile_id}")
async def get_user_profile(
        user_profile_id: str,
        async_session: async_sessionmaker[AsyncSession] = Depends(get_db)
) -> Optional[UserProfile]:
    return await controller.get_user_profile_by_id.process(
        user_profile_id=user_profile_id,
        async_session=async_session
    )


@router.put("/{user_profile_id}")
async def update_user_profile(
        user_profile_id: str,
        user_profile_updates: UserProfileUpdateModel,
        async_session: async_sessionmaker[AsyncSession] = Depends(get_db)
):

    return await controller.update_user_profile.process(
        user_profile_id=user_profile_id,
        user_profile_updates=user_profile_updates,
        async_session=async_session
    )


@router.post("/")
async def create_user_profile(
        user_profile: UserProfileCreate,
        async_session: async_sessionmaker[AsyncSession] = Depends(get_db)
):
    return await controller.create_user_profile.process(
        user_profile=user_profile,
        async_session=async_session
    )


@router.put("/delete-user/{user_profile_id}")
async def delete_user_profile(
        user_profile_id: str,
        async_session: async_sessionmaker[AsyncSession] = Depends(get_db)
):
    return await controller.delete_user_profile.process(
        user_profile_id=user_profile_id,
        async_session=async_session
    )
