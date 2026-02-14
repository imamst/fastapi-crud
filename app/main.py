from fastapi import FastAPI
from app.core.settings import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION
)
