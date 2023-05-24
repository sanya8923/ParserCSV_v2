from database import metadata, Database
from sqlalchemy import Table, Column, Integer, String, ForeignKey


class UsersTable(Database):

    def __init__(self, data):
        self.data = data
        self.filtered_data = []

    def create_table(self):
        user_table = Table('users_table',
                           metadata,
                           Column('id', Integer, primary_key=True),
                           Column('user_id', Integer, ForeignKey('contacts_table.user_id'), nullable=False),
                           Column('Фамилия'), String(255),
                           Column('Имя', String(255)),
                           Column('Отчество', String(255)),
                           Column('День рождения', String(255)),
                           Column('Возраст', String(255)),
                           Column('Пол', String(255)),
                           Column('Метод оплаты', String(255)))

        metadata.create_all()

    def filtering_data(self):
        keys = ['ФИО', 'День рождения', 'Возраст', 'Пол', 'Метод оплаты']
        full_name_key = 'ФИО'
        l_name_key = 'Фамилия'
        f_name_key = 'Имя'
        patronymic_key = 'Отчество'

        for row in self.data:
            temp = {}
            for key, value in row.items():
                if key in keys:
                    temp[key] = value
            self.filtered_data.append(temp)

        for row in self.filtered_data:
            full_name = row[full_name_key].split()
            row[l_name_key] = full_name[0]
            row[f_name_key] = full_name[1]
            if len(full_name) >= 3:
                row[patronymic_key] = full_name[2]
            del(row[full_name_key])

        return self.filtered_data

    def insert_to_table(self):
        pass
