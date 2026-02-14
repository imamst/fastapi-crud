from app.schema.tea import TeaResponse
from fastapi import APIRouter, Depends, status

from app.utils.query_params import standard_params

tea_router = APIRouter(tags=["Tea"])

@tea_router.get("/teas", status_code=status.HTTP_200_OK)
def get_teas(params = Depends(standard_params)):
    return {"message": "Hello World", "params": params}


@tea_router.post("/teas", status_code=status.HTTP_201_CREATED)
def create_tea():
    return TeaResponse(
        id="1",
        name="Matcha Uji",
        description="Premium ceremonial grade matcha from Uji, Kyoto",
        price=12.99,
        tea_type="green",
        origin="Japan"
    )