from database import engine, metadata, Database
from sqlalchemy import Table, Column, Integer, String, ForeignKey, insert, select


class ContactsTable(Database):

    def __init__(self, data):
        self.data = data
        self.filtered_data = []
        self.contacts_table = Table('contacts_table',
                                metadata,
                                Column('id', Integer, primary_key=True),
                                Column('users_id', Integer),
                                Column('phone', String(255)))
        metadata.create_all(engine)

    def insert_to_table(self):
        stmt = insert(self.contacts_table).values(self.filtered_data)

        with engine.connect() as conn:
            conn.execute(stmt)

            conn.commit()

