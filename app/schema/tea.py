from typing import Optional
from pydantic import BaseModel

class TeaRequest(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tea_type: str  # e.g. "green", "black", "oolong", "herbal"
    origin: str  # e.g. "China", "Japan", "India"

class TeaResponse(BaseModel):
    id: str
    name: str
    description: str
    price: float
    tea_type: str
    origin: str
