from sqlalchemy import create_engine, MetaData
from abc import ABC, abstractmethod
from sqlalchemy_utils import database_exists, create_database


engine = create_engine('mysql+pymysql://root:pajd6284jdk@localhost/db_parser')
if not database_exists(engine.url):
    create_database(engine.url)
metadata = MetaData()


class Database(ABC):

    @abstractmethod
    def insert_to_table(self):
        pass

    @abstractmethod
    def filtering_data(self):
        pass

    @abstractmethod
    def select_table(self):
        pass
