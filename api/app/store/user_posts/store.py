from app.store.user_posts.model.user_post import UserPostCreate
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from app.store.user_posts import database


async def get_post(
        user_post_id: str,
        async_session: async_sessionmaker[AsyncSession]
) -> str:
    get_post = await database.get_post(
        user_post_id=user_post_id,
        async_session=async_session,
    )

    return get_post


async def create_user_post(
        user_post: UserPostCreate,
        user_profile_id: str,
        async_session: async_sessionmaker[AsyncSession]
) -> str:
    create_user_post = await database.create_user_post(
        user_post=user_post,
        async_session=async_session,
        user_profile_id=user_profile_id
    )

    return create_user_post


async def delete_user_post(
        user_post_id: str,
        async_session: async_sessionmaker[AsyncSession]
) -> str:

    delete_user_post = await database.delete_user_post(
        user_post_id=user_post_id,
        async_session=async_session
    )

    return delete_user_post
