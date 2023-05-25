from database import engine, metadata, Database
from sqlalchemy import Table, Column, Integer, String, ForeignKey, insert, select, delete


class UsersTable(Database):

    def __init__(self, data):
        self.data = data
        self.user_table = Table('users_table',
                                metadata,
                                Column('user_id', Integer, primary_key=True),
                                Column('last_name', String(255)),
                                Column('first_name', String(255)),
                                Column('patronymic', String(255)),
                                Column('birthday', String(255)),
                                Column('age', String(255)),
                                Column('gender', String(255)),
                                Column('pay_method', String(255)))
        metadata.create_all(engine)

    def filtering_data(self):
        keys = ['ФИО', 'День рождения', 'Возраст', 'Пол', 'Метод оплаты']
        full_name_key = 'ФИО'
        l_name_key = 'Фамилия'
        f_name_key = 'Имя'
        patronymic_key = 'Отчество'

        filtered_data = []

        for row in self.data:
            temp = {}
            for key, value in row.items():
                if key in keys:
                    temp[key] = value
            filtered_data.append(temp)

        for row in filtered_data:
            full_name = row[full_name_key].split()
            row[l_name_key] = full_name[0]
            row[f_name_key] = full_name[1]
            if len(full_name) >= 3:
                row[patronymic_key] = full_name[2]
            else:
                row[patronymic_key] = ''
            del (row[full_name_key])

        return filtered_data

    def insert_to_table(self):
        with engine.begin() as conn:
            for row in self.filtering_data():
                if not self.select_table():
                    stmt = insert(self.user_table).values(
                        last_name=row['Фамилия'],
                        first_name=row['Имя'],
                        patronymic=row['Отчество'],
                        birthday=row['День рождения'],
                        age=row['Возраст'],
                        gender=row['Пол'],
                        pay_method=row['Метод оплаты']
                    )
                conn.execute(stmt)

            conn.commit()

    def select_table(self) -> list:
        stmt = select(self.user_table)

        with engine.connect() as conn:
            result = conn.execute(stmt).fetchall()
            conn.commit()
        return result
