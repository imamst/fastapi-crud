from app.schema.tea import TeaResponse
from fastapi import APIRouter

tea_router = APIRouter(tags=["Tea"])

@tea_router.get("/teas")
def get_teas():
    return TeaResponse(
        id="1",
        name="Matcha Uji",
        description="Premium ceremonial grade matcha from Uji, Kyoto",
        price=12.99,
        tea_type="green",
        origin="Japan"
    )


@tea_router.post("/teas")
def create_tea():
    return TeaResponse(
        id="1",
        name="Matcha Uji",
        description="Premium ceremonial grade matcha from Uji, Kyoto",
        price=12.99,
        tea_type="green",
        origin="Japan"
    )