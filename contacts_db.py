from database import engine, metadata, Database
from sqlalchemy import Table, Column, Integer, String, ForeignKey, insert, select, delete


class ContactsTable(Database):

    def __init__(self, data):
        self.data = data
        self.contacts_table = Table('contacts_table',
                                    metadata,
                                    Column('id', Integer, primary_key=True),
                                    Column('user_id', Integer, ForeignKey('users_table.user_id'), nullable=False),
                                    Column('phone', String(255)))
        metadata.create_all(engine)

    def filtering_data(self):
        keys = ['user_id', 'Телефон']
        filtered_data = []

        for row in self.data:
            temp = {}
            for key, value in row.items():
                if key in keys:
                    temp[key] = value
            filtered_data.append(temp)

        return filtered_data

    def insert_to_table(self):

        with engine.begin() as conn:
            for row in self.filtering_data():
                stmt = insert(self.contacts_table).values(user_id=row['user_id'],
                                                          phone=row['Телефон'])
                conn.execute(stmt)

            conn.commit()

    def select_table(self) -> list:
        stmt = select(self.contacts_table)

        with engine.connect() as conn:
            result = conn.execute(stmt).fetchall()
            conn.commit()
        return result

