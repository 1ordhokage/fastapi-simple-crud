from sqlmodel import SQLModel

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import DATABASE_URL

engine = create_async_engine(DATABASE_URL, echo=True, future=True)


async def init_db():
    """Database initialization"""
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession:
    """Retrieve the current session"""
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session