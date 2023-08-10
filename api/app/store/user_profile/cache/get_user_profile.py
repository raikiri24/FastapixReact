import json
from typing import Optional
from app.config import settings
from app.service.cache.cache import redis
from pydantic.json import pydantic_encoder
from app.store.user_profile.model.user_profile import UserProfile

_key = 'user_profile'
_ttl = settings.redis_cache_ttl


async def get_user_profile(
        user_profile_id: str,
) -> Optional[UserProfile]:
    user_profile_str = await redis.get(f'{_key}:user_profile_id:{user_profile_id}')

    if user_profile_str:
        return UserProfile.parse_raw(user_profile_str)


async def set_user_profile(
        user_profile_id: str,
        user_profile: UserProfile
):
    serialized = json.dumps(user_profile,
                            default=pydantic_encoder)

    return await redis.setex(f'{_key}:user_profile_id:{user_profile_id}', _ttl, serialized)
