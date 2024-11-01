from src.resources.orders import Orders



class OrdersService(object):

    table = None

    def __init__(self):
        self.table = Orders()

    def get_all(self, skip: int, limit: int) -> list:
        return self.table.get_all(skip, limit)
    
    def add_one(self, order: dict) -> dict:
        return self.table.add_one(order)