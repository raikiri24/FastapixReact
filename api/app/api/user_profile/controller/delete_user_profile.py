from app.store.user_profile.model.user_profile import UserProfileUpdateModel
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from app.store.user_profile import store as user_profile_store


async def process(
        user_profile_id: str,
        async_session: async_sessionmaker[AsyncSession]
):
    return await user_profile_store.delete_user_profile(
        user_profile_id=user_profile_id,
        async_session=async_session
    )
