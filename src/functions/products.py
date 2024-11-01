from fastapi import APIRouter, Path, Body, Query

from src.services.products import ProductsService
from src.entities.schemas.products import ProductSchema

products_router = APIRouter(prefix="/products")

@products_router.get(path="", response_model=list[ProductSchema])
def get_products(skip: int = Query(0, title="The number of products to skip"),
                 limit: int = Query(10, title="The number of products to return")):
    return ProductsService().get_all(skip, limit)


@products_router.post(path="", response_model=ProductSchema)
def create_product(product: ProductSchema = Body(...)):
    return ProductsService().add_one(product.dict())

@products_router.put(path="/{product_id}", response_model=ProductSchema)
def update_product(product_id: int = Path(..., title="The ID of the product to update"),
                   product: ProductSchema = Body(...)):
    return ProductsService().update_one(product_id, product.dict())

@products_router.delete(path="/{product_id}", response_model=ProductSchema)
def delete_product(product_id: int = Path(..., title="The ID of the product to delete")):
    return ProductsService().delete_one(product_id)