from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference
from app.core.settings import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION
)

@app.get("/scalar")
def get_scalar():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title
    )