from database import engine

from sqlalchemy import MetaData


class Base:
    metadata = MetaData()
