from redis import asyncio as aioredis

from app.config import settings

redis_url = settings.redis_url.format(
    redis_host=settings.redis_host,
    redis_port=settings.redis_port
)

if settings.redis_ssl:
    redis = aioredis.from_url(
        redis_url,
        db=settings.redis_db,
        password=settings.redis_password,
        decode_responses=settings.redis_decode_response,
        ssl=True,
        ssl_cert_reqs=None
    )
else:
    redis = aioredis.from_url(
        redis_url,
        db=settings.redis_db,
        password=settings.redis_password,
        decode_responses=settings.redis_decode_response
    )
