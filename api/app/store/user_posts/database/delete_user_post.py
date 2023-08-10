from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from app.store.user_posts.model.user_post import UserPost
from app.store.user_posts.schema.user_post import Posts as PostSchema
from sqlalchemy import update
from fastapi import HTTPException
from pydantic import parse_obj_as
from app.logging import logger
from time import time


async def delete_user_post(
        user_post_id: str,
        async_session: async_sessionmaker[AsyncSession]
) -> str:
    async with async_session() as session:
        async with session.begin():
            try:
                time_now = time()
                deleted_user_post = update(PostSchema)\
                    .where(PostSchema.id == user_post_id)\
                    .values(
                        deleted_at=time_now,
                        updated_at=time_now
                )

                await session.execute(deleted_user_post)
                return "Deleted"
            except Exception as e:
                await session.rollback()

                logger.error(
                    f'[database.deleted_user_post] Exception: {e}')
                raise HTTPException(
                    status_code=500, detail="Database exception")
