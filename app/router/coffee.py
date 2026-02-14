from sqlmodel import select
from app.models.database import Coffee
from app.models.engine import get_db
from app.schema.coffee import CoffeeResponse
from fastapi import APIRouter, Depends, status

from app.utils.query_params import standard_params

coffee_router = APIRouter(tags=["Coffee"])

@coffee_router.get("/coffees", status_code=status.HTTP_200_OK)
def get_coffees(params = Depends(standard_params), db = Depends(get_db)):
    coffees = db.exec(select(Coffee)).all()
    return [CoffeeResponse.model_validate(coffee) for coffee in coffees]

@coffee_router.post("/coffees", status_code=status.HTTP_201_CREATED)
def create_coffee():
    return CoffeeResponse(
        id="1",
        name="Ethiopia Yirgacheffe",
        description="Bright and fruity single-origin coffee",
        price=15.99,
        roast_level="light",
        origin="Ethiopia"
    )