from app.store.user_profile.schema.user_profile import UserProfile as UserProfileSchema
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from app.store.user_profile.model.user_profile import UserProfile
from fastapi import HTTPException
from pydantic import parse_obj_as
from app.logging import logger
from sqlalchemy import update
from time import time


from sqlalchemy import select


async def delete_user_profile(
        user_profile_id: str,
        async_session: async_sessionmaker[AsyncSession]
) -> str:
    async with async_session() as session:
        async with session.begin():
            try:
                time_now = time()

                deleted_user_profile = update(UserProfileSchema)\
                    .where(UserProfileSchema.id == user_profile_id)\
                    .values(
                        deleted_at=time_now,
                        updated_at=time_now
                )

                await session.execute(deleted_user_profile)
                return 'Deleted'

            except Exception as e:
                await session.rollback()

                logger.error(
                    f'[database.delete_user_profile] Exception: {e}')
                raise HTTPException(
                    status_code=500, detail="Database exception")
