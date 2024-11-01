from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import declarative_base

Base = declarative_base()
metadata = Base.metadata

class TblProducts(Base):
    __tablename__ = "tblProducts"

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    category = Column(String(40), nullable=False)
    price = Column(Numeric(7, 2), nullable=False)
    stock = Column(Integer, nullable=False)
    image = Column(String(100), nullable=True)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
