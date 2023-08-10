from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from app.store.user_posts.model.user_post import UserPostCreate
from app.store.user_posts.schema.user_post import Posts as PostSchema
from sqlalchemy import insert, select
from fastapi import HTTPException
from pydantic import parse_obj_as
from app.logging import logger
from time import time


async def create_user_post(
        user_profile_id: str,
        user_post: UserPostCreate,
        async_session: async_sessionmaker[AsyncSession]
) -> str:
    async with async_session() as session:
        async with session.begin():
            try:
                time_now = time()
                created_user_profile = insert(PostSchema)\
                    .values(
                        title=user_post.title,
                        description=user_post.description,
                        owner_id=user_profile_id,
                        created_at=time_now,
                        updated_at=time_now
                )

                await session.execute(created_user_profile)
                return "Posted"
            except Exception as e:
                await session.rollback()

                logger.error(
                    f'[database.created_user_profile] Exception: {e}')
                raise HTTPException(
                    status_code=500, detail="Database exception")
