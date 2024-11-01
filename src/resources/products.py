from src.entities.models.products import TblProducts
from src.resources.session import Database

class Products():

    def __init__(self):
        self.db = Database()
        self.table = TblProducts

    def get_one(self, product_id: int) -> dict:
        product = self.db.get_one(self.table, product_id)
        return product.as_dict()

    def get_all(self, skip: int = 0, limit: int = 10) -> list:
        products = self.db.get_all(self.table, skip, limit)
        return list(map(lambda product: product.as_dict(), products))

    def add_one(self, product: dict) -> dict:
        new_product = self.db.add_one(self.table, product)
        return new_product.as_dict()

    def update_one(self, product_id: int, product: dict) -> dict:
        updated_product = self.db.update_one(self.table, product_id, product)
        return updated_product.as_dict()
    
    def delete_one(self, product_id: int) -> dict:
        deleted_product = self.db.delete_one(self.table, product_id)
        return deleted_product.as_dict()