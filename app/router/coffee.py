from sqlmodel import select
from app.models.database import Coffee
from app.models.engine import get_db
from app.schema.coffee import CoffeeRequest, CoffeeResponse
from fastapi import APIRouter, Depends, status, HTTPException

from app.utils.query_params import standard_params

coffee_router = APIRouter(tags=["Coffee"])

@coffee_router.get("/coffees", status_code=status.HTTP_200_OK)
def get_coffees(params = Depends(standard_params), db = Depends(get_db)):
    coffees = db.exec(select(Coffee)).all()
    return {"coffees": coffees}

@coffee_router.post("/coffees", status_code=status.HTTP_201_CREATED)
def create_coffee(request: CoffeeRequest, db = Depends(get_db)):
    new_coffee = Coffee(
        name=request.name,
        description=request.description,
        price=request.price,
        roast_level=request.roast_level,
        origin=request.origin
    )
    db.add(new_coffee)
    db.commit()
    db.refresh(new_coffee)

    return new_coffee

@coffee_router.get("/coffees/{id}", status_code=status.HTTP_200_OK)
def get_coffee(id: int, db = Depends(get_db)):
    coffee = db.get(Coffee, id)
    if not coffee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Coffee not found")
    return coffee

@coffee_router.put("/coffees/{id}", status_code=status.HTTP_200_OK)
def update_coffee(id: int, request: CoffeeRequest, db = Depends(get_db)):
    coffee = db.get(Coffee, id)
    if not coffee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Coffee not found")
    coffee.name = request.name
    coffee.description = request.description
    coffee.price = request.price
    coffee.roast_level = request.roast_level
    coffee.origin = request.origin
    db.commit()
    db.refresh(coffee)
    return coffee