from fastapi import APIRouter, Body, Query

from src.services.orders import OrdersService
from src.entities.schemas.orders import OrderSchema

orders_router = APIRouter(prefix="/orders")

@orders_router.get(path="", response_model=list[OrderSchema])
def get_orders(skip: int = Query(0, title="The number of orders to skip"),
                 limit: int = Query(10, title="The number of orders to return")):
    return OrdersService().get_all(skip, limit)


@orders_router.post(path="", response_model=OrderSchema)
def create_order(order: OrderSchema = Body(...)):
    return OrdersService().add_one(order.dict())