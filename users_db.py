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
                           Column('last_name'), String(255),
                           Column('first_name', String(255)),
                           Column('patronymic', String(255)),
                           Column('birthday', String(255)),
                           Column('gender', String(255)),
                           Column('pay_method', String(255)))

        metadata.create_all()

    def filtering_data(self):
        keys = ['ФИО', 'День рождения', 'Возраст', 'Пол', 'Метод оплаты']
        full_name_key = 'ФИО'
        l_name_key = 'Фамилия'
        f_name_key = 'Имя'
        patronymic_key = 'Отчество'

        for row_data in self.data:
            temp = {}
            for key, value in row_data.items():
                if key in keys:
                    temp[key] = value
            self.filtered_data.append(temp)


        # for row in self.filtered_data:
        #     row[l_name_key] = full_name_key.split()[0]
        #     row[f_name_key] = full_name_key.split()[1]
        #     row[patronymic_key] = full_name_key.split()[2]

        return self.filtered_data


    def entry_table(self):
        pass