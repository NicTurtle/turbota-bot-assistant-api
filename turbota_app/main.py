from fastapi import FastAPI
from contextlib import asynccontextmanager
import asyncio
from turbota_app.bot import start_bot  # обновлённый импорт
from turbota_app.routers import base

@asynccontextmanager
async def lifespan(app: FastAPI):
    asyncio.create_task(start_bot())
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(base.router)
