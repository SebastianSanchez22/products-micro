from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from src.config.env import DATABASE_CREDENTIALS

class Database():
    __instance = None
    session = None

    def __new__(cls, *args, **kwargs):
        if Database.__instance is None:
            Database.__instance = object.__new__(cls)
        return Database.__instance

    def __init__(self):
        if self.session is None:
            self.engine = create_engine(DATABASE_CREDENTIALS, poolclass=NullPool)
            self.session = self._create_session()

    def _create_session(self) -> sessionmaker:
        metadata = MetaData()
        metadata.reflect(bind=self.engine)
        session = sessionmaker(bind=self.engine)
        return session()
    
    def __del__(self):
        if self.session:
            self.session.close()
    
    def get_one(self, **kwargs) -> dict:
        try:
            query = self.session.query(kwargs['table'])
            if 'filter' in kwargs:
                query = query.filter_by(**kwargs['filter'])
            product = query.first()
            return product
        except Exception as e:
            self.session.rollback()
            raise e


    def get_all(self, table, skip: int, limit: int) -> list:
        try:
            products = self.session.query(table).offset(skip).limit(limit).all()
            return products
        except Exception as e:
            self.session.rollback()
            raise e

    def add_one(self, table, product: dict) -> dict:
        try:
            new_product = table(**product)
            self.session.add(new_product)
            self.session.commit()
            return new_product
        except Exception as e:
            self.session.rollback()
            raise e

    def update_one(self, table, product_id: int, product: dict) -> dict:
        try:
            updated_product = self.session.query(table).filter(table.id == product_id).update(product)
            self.session.commit()
            return updated_product
        except Exception as e:
            self.session.rollback()
            raise e

    def delete_one(self, table, product_id: int) -> dict:
        try:
            deleted_product = self.session.query(table).filter(table.id == product_id).delete()
            self.session.commit()
            return deleted_product
        except Exception as e:
            self.session.rollback()
            raise e