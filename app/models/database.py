from sqlmodel import Field, SQLModel


class Coffee(SQLModel, table=True):
    id: int | None = Field(primary_key=True)
    name: str = Field(default="Kopi Luwak")
    description: str | None = Field(default="A coffee from Indonesia")
    price: float = Field(default=10.0)
    roast_level: str = Field(default="Medium")
    origin: str = Field(default="Indonesia")


class Tea(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(default="Matcha Uji")
    description: str | None = Field(default="Premium ceremonial grade matcha")
    price: float = Field(default=12.99)
    tea_type: str = Field(default="green")
    origin: str = Field(default="Japan")
