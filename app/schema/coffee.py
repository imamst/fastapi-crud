from typing import Optional
from pydantic import BaseModel

class CoffeeRequest(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    roast_level: str  # e.g. "light", "medium", "dark"
    origin: str  # e.g. "Ethiopia", "Colombia", "Brazil"

class CoffeeResponse(BaseModel):
    id: str
    name: str
    description: str
    price: float
    roast_level: str
    origin: str
