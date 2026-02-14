from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference
from app.core.settings import settings
from app.router.auth import auth_router
from app.router.coffee import coffee_router
from app.router.tea import tea_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION
)

app.include_router(coffee_router)
app.include_router(tea_router)
app.include_router(auth_router)

@app.get("/scalar")
def get_scalar():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title
    )