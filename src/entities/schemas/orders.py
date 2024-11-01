from datetime import date
from pydantic import BaseModel

class OrderSchema(BaseModel):
    product_id: int
    customer_name: str
    customer_email: str
    quantity: int
    order_date: date
    destination_city: str