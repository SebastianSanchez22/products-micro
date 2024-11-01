from src.entities.models.orders import TblOrders
from src.entities.models.products import TblProducts
from src.resources.session import Database

class Orders():

    def __init__(self):
        self.db = Database()
        self.table = TblOrders
        self.products_table = TblProducts

    def get_all(self, skip: int = 0, limit: int = 10) -> list:
        orders = self.db.get_all(self.table, skip, limit)
        return list(map(lambda order: order.as_dict(), orders))

    def add_one(self, order: dict) -> dict:
        product_id = order.get("product_id")
        quantity = order.get("quantity")
        product = self.db.get_one(
            table=self.products_table, 
            filter={"id": product_id}
        )
        if product.stock < quantity:
            raise ValueError("Not enough products")
        product.stock -= quantity
        self.db.update_one(self.products_table, product_id, product.as_dict())
        new_order = self.db.add_one(self.table, order)
        return new_order.as_dict()