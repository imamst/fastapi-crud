from app.schema.coffee import CoffeeResponse
from fastapi import APIRouter

coffee_router = APIRouter(tags=["Coffee"])

@coffee_router.get("/coffees")
def get_coffees():
    return CoffeeResponse(
        id="1",
        name="Ethiopia Yirgacheffe",
        description="Bright and fruity single-origin coffee",
        price=15.99,
        roast_level="light",
        origin="Ethiopia"
    )

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