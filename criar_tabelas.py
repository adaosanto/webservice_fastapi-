import asyncio

from core.database import engine
from core.config import settings

async def create_tables() -> None:
    import models.__all_models
    async with engine.begin() as conn:
        await conn.run_sync(settings.DBModelBase.metadata.drop_all)
        await conn.run_sync(settings.DBModelBase.metadata.create_all)

if __name__ == '__main__':
    asyncio.run(create_tables())