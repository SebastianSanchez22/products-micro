
from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import backref, Relationship

from src.entities.models.products import Base, TblProducts

class TblOrders(Base):
    __tablename__ = "tblOrders"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("tblProducts.id"))
    customer_name = Column(String(50), nullable=False)
    customer_email = Column(String(50), nullable=False)
    quantity = Column(Integer, nullable=False)
    order_date = Column(Date, nullable=False)
    total_price = Column(Float, nullable=False)
    destination_city = Column(String(50), nullable=False)
    products = Relationship(TblProducts, backref= backref("products_details", cascade="all, delete-orphan"))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}