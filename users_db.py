from database import metadata
from sqlalchemy import Table, Column, Integer, String, ForeignKey


class UsersTable:

    def __init__(self, data: list):
        self.data = data
        self.filtered_data = []

    def create_table(self):
        user_table = Table('users_table',
                           metadata,
                           Column('id', Integer, primary_key=True),
                           Column('user_id', Integer, ForeignKey('contacts_table.user_id'), nullable=False),
                           Column('last_name'), String(255),
                           Column('first_name', String(255)),
                           Column('patronymic', String(255)),
                           Column('birthday', String(255)),
                           Column('gender', String(255)),
                           Column('pay_method', String(255)))

        metadata.create_all()

    def filtering_data(self):
        keys = ['ФИО', 'День рождения', 'Возраст', 'Пол', 'Метод оплаты']

        for row in self.data:
            self.filtered_data = {key: value for key, value in row.items() if key in keys}

    def entry_table(self):
        pass

