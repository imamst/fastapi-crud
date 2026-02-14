from sqlmodel import select
from app.models.database import Tea
from app.models.engine import get_db
from app.schema.tea import TeaRequest
from fastapi import APIRouter, Depends, status, HTTPException

from app.utils.query_params import standard_params

tea_router = APIRouter(tags=["Tea"])

@tea_router.get("/teas", status_code=status.HTTP_200_OK)
def get_teas(params = Depends(standard_params), db = Depends(get_db)):
    teas = db.exec(select(Tea)).all()
    return {"teas": teas}

@tea_router.post("/teas", status_code=status.HTTP_201_CREATED)
def create_tea(request: TeaRequest, db = Depends(get_db)):
    new_tea = Tea(
        name=request.name,
        description=request.description,
        price=request.price,
        tea_type=request.tea_type,
        origin=request.origin
    )
    db.add(new_tea)
    db.commit()
    db.refresh(new_tea)

    return new_tea

@tea_router.get("/teas/{id}", status_code=status.HTTP_200_OK)
def get_tea(id: int, db = Depends(get_db)):
    tea = db.get(Tea, id)
    if not tea:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tea not found")
    return tea

@tea_router.put("/teas/{id}", status_code=status.HTTP_200_OK)
def update_tea(id: int, request: TeaRequest, db = Depends(get_db)):
    tea = db.get(Tea, id)
    if not tea:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tea not found")
    tea.name = request.name
    tea.description = request.description
    tea.price = request.price
    tea.tea_type = request.tea_type
    tea.origin = request.origin
    db.commit()
    db.refresh(tea)
    return tea

@tea_router.delete("/teas/{id}", status_code=status.HTTP_200_OK)
def delete_tea(id: int, db = Depends(get_db)):
    tea = db.get(Tea, id)
    if not tea:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tea not found")
    db.delete(tea)
    db.commit()
    return {"message": "Tea deleted successfully"}
