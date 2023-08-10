from app.store.user_profile.schema.user_profile import UserProfile as UserProfileSchema
from app.store.user_profile.model.user_profile import UserProfile as UserProfileModel
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from pydantic import parse_obj_as
from fastapi import HTTPException
from app.logging import logger
from sqlalchemy import select
from typing import Optional


async def get_user_profile_by_id(
        user_profile_id: str,
        async_session: async_sessionmaker[AsyncSession]
):
    '''RETURN SOMETHING'''
    async with async_session() as session:
        async with session.begin():
            try:
                query = select(UserProfileSchema).filter_by(
                    id=user_profile_id)

                result = await session.execute(query)

                user_profile = result.scalar_one_or_none()
                logger.debug(f">>>{user_profile}")
                if user_profile:
                    logger.debug(f">>>here")
                    return parse_obj_as(UserProfileModel, user_profile)

            except Exception as e:
                logger.error(
                    f'[database.get_user_profile_by_id] Exception: {e}')
                raise HTTPException(
                    status_code=500, detail="Database exception")
