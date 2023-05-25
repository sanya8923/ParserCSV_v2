from database import Database, engine
from sqlalchemy import select


class DatabaseFinder(Database):
    def __init__(self, users_db_obj, contacts_db_obj):
        self.users = users_db_obj
        self.contacts = contacts_db_obj

    def find_user_by_phone(self, phone):

        stmt_sel_user_id = select(self.contacts.contacts_table.c.user_id)\
            .where(self.contacts.contacts_table.c.phone == f"{phone}")\
            .scalar_subquery()
        stmt_sel_user_info = select(self.users.user_table).\
            where(self.users.user_table.c.user_id == stmt_sel_user_id)

        gen_res = ''

        with engine.connect() as conn:
            result = conn.execute(stmt_sel_user_info)

            for row in result:
                for item in row:
                    gen_res = gen_res + ' ' + item
            conn.commit()

        print(result)

