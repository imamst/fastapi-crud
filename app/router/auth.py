from app.schema.login import LoginRequest
from app.schema.login import LoginResponse
from fastapi import APIRouter, status, HTTPException

auth_router = APIRouter(tags=["Auth"])

@auth_router.post("/login", status_code=status.HTTP_200_OK)
def login(request: LoginRequest):
    if request.email != "test@test.com":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid credentials")

    return LoginResponse(
        access_token="1234567890",
        refresh_token="1234567890"
    )
