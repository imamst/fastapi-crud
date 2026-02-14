from app.schema.coffee import CoffeeResponse
from fastapi import APIRouter, Depends

from app.utils.query_params import standard_params

coffee_router = APIRouter(tags=["Coffee"])

@coffee_router.get("/coffees")
def get_coffees(params = Depends(standard_params)):
    return {"message": "Hello World", "params": params}

@coffee_router.post("/coffees")
def create_coffee():
    return CoffeeResponse(
        id="1",
        name="Ethiopia Yirgacheffe",
        description="Bright and fruity single-origin coffee",
        price=15.99,
        roast_level="light",
        origin="Ethiopia"
    )