from app.store.user_posts.model.user_post import UserPostCreate
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from app.service.database.database import get_db
from app.api.user_post import controller
from fastapi import APIRouter, Depends


router = APIRouter(
    prefix="/api/post",
)


@router.get("/{post_id}")
async def get_post(
        user_post_id: str,
        async_session: async_sessionmaker[AsyncSession] = Depends(get_db)
):
    return await controller.get_post.process(
        user_post_id=user_post_id,
        async_session=async_session
    )


@router.post("/")
async def create_user_post(
        user_post: UserPostCreate,
        user_profile_id: str,
        async_session: async_sessionmaker[AsyncSession] = Depends(get_db)
):
    return await controller.create_user_post.process(
        user_post=user_post,
        user_profile_id=user_profile_id,
        async_session=async_session
    )


@router.put("/delete-user/{user_profile_id}")
async def delete_user_profile(
        user_profile_id: str,
        async_session: async_sessionmaker[AsyncSession] = Depends(get_db)
):
    return await controller.delete_user_profile.process(
        user_profile_id=user_profile_id,
        async_session=async_session
    )
