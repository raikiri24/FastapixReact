from app.store.user_posts.schema.user_post import Posts as PostSchema
from app.store.user_posts.model.get_user_post import GetUserPost
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from pydantic import parse_obj_as
from fastapi import HTTPException
from app.logging import logger
from sqlalchemy import select


async def get_post(
        user_post_id: str,
        async_session: async_sessionmaker[AsyncSession]
):
    '''RETURN SOMETHING'''
    async with async_session() as session:
        async with session.begin():
            try:
                query = select(PostSchema).filter_by(
                    id=user_post_id)

                result = await session.execute(query)

                user_post = result.scalar_one_or_none()
                if user_post:
                    return parse_obj_as(GetUserPost, user_post)

            except Exception as e:
                logger.error(
                    f'[database.get_post] Exception: {e}')
                raise HTTPException(
                    status_code=500, detail="Database exception")
