from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from src.functions.products import products_router
from src.functions.orders import orders_router

app = FastAPI()
main_router = APIRouter()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

main_router.include_router(orders_router)
main_router.include_router(products_router)

app.include_router(main_router)
