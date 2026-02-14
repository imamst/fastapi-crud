from app.schema.coffee import CoffeeResponse
from fastapi import APIRouter

coffee_router = APIRouter()

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