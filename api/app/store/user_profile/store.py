from app.store.user_profile.model.user_profile import UserProfile, UserProfileUpdateModel, UserProfileCreate
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from app.store.user_profile import database, cache
from typing import Optional


async def get_user_profile_by_id(
        user_profile_id: str,
        async_session: async_sessionmaker[AsyncSession]
):
    user_profile = await cache.get_user_profile(
        user_profile_id=user_profile_id,
    )

    if user_profile is None:
        user_profile = await database.get_user_profile_by_id(
            user_profile_id=user_profile_id,
            async_session=async_session
        )
        await cache.set_user_profile(
            user_profile_id=user_profile_id,
            user_profile=user_profile,
        )

    return user_profile


async def update_user_profile(
        user_profile_id: str,
        user_profile_updates: UserProfileUpdateModel,
        async_session: async_sessionmaker[AsyncSession]
) -> UserProfile:
    updated_user_profile = await database.update_user_profile(
        user_profile_id=user_profile_id,
        user_profile_updates=user_profile_updates,
        async_session=async_session
    )

    return updated_user_profile


async def create_user_profile(
        user_profile: UserProfileCreate,
        async_session: async_sessionmaker[AsyncSession]
) -> str:
    create_user_profile = await database.create_user_profile(
        user_profile=user_profile,
        async_session=async_session
    )

    return create_user_profile


async def delete_user_profile(
        user_profile_id: str,
        async_session: async_sessionmaker[AsyncSession]
) -> str:

    delete_user_profile = await database.delete_user_profile(
        user_profile_id=user_profile_id,
        async_session=async_session
    )

    return delete_user_profile
