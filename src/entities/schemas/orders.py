from typing import Optional
from pydantic import BaseModel

class OrderSchema(BaseModel):
    product_id: int
    customer_name: str
    customer_email: str
    quantity: int
    order_date: str
    total_price: int
    destination_city: str