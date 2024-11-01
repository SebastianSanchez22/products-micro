from typing import Optional
from pydantic import BaseModel

class ProductSchema(BaseModel):
    name: str
    category: str
    price: float
    stock: int
    image: Optional[str] = None