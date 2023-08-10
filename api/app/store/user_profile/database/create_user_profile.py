
from app.store.user_profile.model.user_profile import UserProfile, UserProfileCreate
from app.store.user_profile.schema.user_profile import UserProfile as UserProfileSchema
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from passlib.context import CryptContext
from sqlalchemy import insert, select
from fastapi import HTTPException
from pydantic import parse_obj_as
from app.logging import logger
from time import time


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")





async def create_user_profile(
        user_profile: UserProfileCreate,
        async_session: async_sessionmaker[AsyncSession]
) -> str:
    async with async_session() as session:
        async with session.begin():
            try:
                time_now = time()
                created_user_profile = insert(UserProfileSchema)\
                    .values(
                        user_name=user_profile.user_name,
                        email=user_profile.email,
                        first_name=user_profile.first_name,
                        middle_name=user_profile.middle_name,
                        last_name=user_profile.last_name,
                        password=user_profile.password,
                        birthday=user_profile.birthday,
                        address=user_profile.address,
                        is_active=user_profile.is_active,
                        phone_number=user_profile.phone_number,
                        created_at=time_now,
                        updated_at=time_now
                )

                await session.execute(created_user_profile)

                return "Inserted"
            except Exception as e:
                await session.rollback()

                logger.error(
                    f'[database.create_user_profile] Exception: {e}')
                raise HTTPException(
                    status_code=500, detail="Database exception")
