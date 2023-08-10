from app.store.user_profile.model.user_profile import UserProfileCreate
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from app.store.user_posts import store as user_post_store
from app.store.user_posts.model.user_post import UserPostCreate


async def process(
        user_profile_id: str,
        user_post: UserPostCreate,
        async_session: async_sessionmaker[AsyncSession]
):
    return await user_post_store.create_user_post(
        user_post=user_post,
        user_profile_id=user_profile_id,
        async_session=async_session
    )
