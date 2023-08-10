from app.store.user_profile.model.user_profile import UserProfileCreate
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from app.store.user_profile import store as user_profile_store


async def process(
        user_profile: UserProfileCreate,
        async_session: async_sessionmaker[AsyncSession]
):
    return await user_profile_store.create_user_profile(
        user_profile=user_profile,
        async_session=async_session
    )
