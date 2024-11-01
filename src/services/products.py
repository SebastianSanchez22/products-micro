from src.resources.products import Products

class ProductsService(object):

    table = None

    def __init__(self):
        self.table = Products()

    def get_all(self, skip: int, limit: int) -> list:
        return self.table.get_all(skip, limit)

    def add_one(self, product: dict) -> dict:
        return self.table.add_one(product)

    def update_one(self, product_id: int, product: dict) -> dict:
        return self.table.update_one(product_id, product)

    def delete_one(self, product_id: int) -> dict:
        return self.table.delete_one(product_id)