from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from src.config.env import DATABASE_CREDENTIALS

class Database():

    def __new__(cls, *args, **kwargs):
        if Database.__instance is None:
            Database.__instance = object.__new__(cls)
        return Database.__instance

    def __init__(self):
        if self.session is None:
            self.engine = create_engine(DATABASE_CREDENTIALS)
            self.Session = self.__create_session(self.engine)

    def _create_session(self, url) -> sessionmaker:
        engine = create_engine(url, poolclass=NullPool)
        metadata = MetaData()
        metadata.reflect(bind=engine)
        session = sessionmaker(bind=engine)
        return session()


    def get_all(self, table, skip: int, limit: int) -> list:
        session = self.Session()
        products = session.query(table).offset(skip).limit(limit).all()
        session.close()
        return products

    def add_one(self, table, product: dict) -> dict:
        session = self.Session()
        new_product = table(**product)
        session.add(new_product)
        session.commit()
        session.refresh(new_product)
        session.close()
        return new_product

    def update_one(self, table, product_id: int, product: dict) -> dict:
        session = self.Session()
        updated_product = session.query(table).filter(table.id == product_id).update(product)
        session.commit()
        session.close()
        return updated_product

    def delete_one(self, table, product_id: int) -> dict:
        session = self.Session()
        deleted_product = session.query(table).filter(table.id == product_id).delete()
        session.commit()
        session.close()
        return deleted_product