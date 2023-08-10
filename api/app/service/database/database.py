from app.config import settings
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

DATABASE_URL = settings.database_uri.format(
    mysql_host=settings.mysql_host,
    mysql_user=settings.mysql_user,
    mysql_password=settings.mysql_password,
    mysql_db=settings.mysql_db,
    mysql_charset=settings.mysql_charset
)

engine = create_async_engine(
    DATABASE_URL
)


def get_db():
    async_session = async_sessionmaker(
        engine, autocommit=False, autoflush=False, expire_on_commit=False)
    return async_session


Base = declarative_base()
