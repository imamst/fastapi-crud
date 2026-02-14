import uuid
from sqlmodel import SQLModel, Field

class Coffee(SQLModel, table=True):
    id: int = Field(primary_key=True, default_factory=uuid.uuid4)
    name: str = Field(default="Kopi Luwak")
    description: str = Field(default="A coffee from Indonesia")
    price: float = Field(default=10.0)
    roast_level: str = Field(default="Medium")
    origin: str = Field(default="Indonesia")