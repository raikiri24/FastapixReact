
from app.store.user_profile.model.user_profile import UserProfile, UserProfileUpdateModel
from app.store.user_profile.schema.user_profile import UserProfile as UserProfileSchema
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from passlib.context import CryptContext
from sqlalchemy import update, select
from pydantic import parse_obj_as
from fastapi import HTTPException
from app.logging import logger
from time import time


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    '''
    Encryption ng password
    '''
    return bcrypt_context.hash(password)


async def update_user_profile(
        user_profile_id: str,
        user_profile_updates: UserProfileUpdateModel,
        async_session: async_sessionmaker[AsyncSession]
) -> UserProfile:
    async with async_session() as session:
        async with session.begin():
            try:
                updated_at = time()

                updated_user_profile = update(UserProfileSchema)\
                    .where(UserProfileSchema.id == user_profile_id)\
                    .values(
                        user_name=user_profile_updates.user_name,
                        email=user_profile_updates.email,
                        first_name=user_profile_updates.first_name,
                        last_name=user_profile_updates.last_name,
                        password=get_password_hash(
                            user_profile_updates.password),

                        updated_at=updated_at
                )

                await session.execute(updated_user_profile)

                select_query = select(UserProfileSchema).filter_by(
                    id=user_profile_id)
                result = await session.execute(select_query)
                updated_user_profile = result.scalar_one_or_none()

                if updated_user_profile:
                    return parse_obj_as(UserProfile, updated_user_profile)
            except Exception as e:
                await session.rollback()

                logger.error(
                    f'[database.update_user_profile] Exception: {e}')
                raise HTTPException(
                    status_code=500, detail="Database exception")
