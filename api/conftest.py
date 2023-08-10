
import asyncio

import pytest
from httpx import AsyncClient
from starlette.testclient import TestClient

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.pool import NullPool

from main import app
from app.service.database.database import get_db, Base
from app.config import settings


SQLALCHEMY_DATABASE_URL = settings.sqlalchemy_database_base_uri.format(
    mysql_host=settings.mysql_host,
    mysql_user=settings.mysql_user,
    mysql_password=settings.mysql_password,
    mysql_db=settings.test_mysql_db,
    mysql_charset=settings.mysql_charset,
)

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, poolclass=NullPool
)


async def startup():
    # create db tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(startup())


def override_get_db():
    async_session = async_sessionmaker(
        engine, autocommit=False, autoflush=False, expire_on_commit=False)
    return async_session


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture(autouse=True)
def run_delete_redis(request):
    run_fixture = request.node.get_closest_marker("run_delete_redis")
    if run_fixture:
        return run_fixture.kwargs.get('value', True)
    return False


@pytest.fixture(scope="session")
async def client():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000/") as client:
        print("Client is ready")
        yield client


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "run_delete_redis: run the delete_redis_keys fixture")
