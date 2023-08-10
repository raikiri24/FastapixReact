from app.store.user_profile.model.user_profile import UserProfileCreate
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from app.store.user_posts import store as user_post_store


async def process(
        user_post_id: str,
        async_session: async_sessionmaker[AsyncSession]
):
    return await user_post_store.get_post(
        user_post_id=user_post_id,
        async_session=async_session
    )
