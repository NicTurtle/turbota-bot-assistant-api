from fastapi import FastAPI
import asyncio
from bot import start_bot
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    asyncio.create_task(start_bot())
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "TurbotaBot is running."}
