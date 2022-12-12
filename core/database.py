from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings

# Criação da Engine assíncrona.
engine: AsyncEngine = create_async_engine(settings.DB_URL)

# Criação da Session assíncrona.
Session: AsyncSession = sessionmaker(
    bind=engine, 
    expire_on_commit=False, 
    autocommit=False,
    autoflush=False,
    class_=AsyncSession)
                                