from database import, Database, engine
from sqlalchemy import select


class DatabaseFinder(Database):
    def __init__(self, users_db_obj, contacts_db_obj):
        self.users = users_db_obj
        self.contacts = contacts_db_obj


