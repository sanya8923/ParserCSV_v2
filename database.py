from sqlalchemy import create_engine, MetaData
from abc import ABC, abstractmethod

engine = create_engine('mysql+pymysql://root:pajd6284jdk@localhost/db_parser')
metadata = MetaData()


class Database(ABC):
    @abstractmethod
    def create_table(self):
        pass

    @abstractmethod
    def insert_to_table(self):
        pass

    @abstractmethod
    def filtering_data(self):
        pass
