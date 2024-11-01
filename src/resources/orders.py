from src.entities.models.orders import TblOrders
from src.resources.session import Database

class Orders():

    def __init__(self):
        self.db = Database()
        self.table = TblOrders

    def get_all(self, skip: int = 0, limit: int = 10) -> list:
        orders = self.db.get_all(self.table, skip, limit)
        return list(map(lambda order: order.as_dict(), orders))

    def add_one(self, order: dict) -> dict:
        new_order = self.db.add_one(self.table, order)
        return new_order.as_dict()