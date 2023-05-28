from base import Base
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship, Session
from typing import List, Optional, Any
from database import engine
from contacts_db import Contacts


class Users(Base):
    __tablename__ = 'users_table'

    id: Mapped[int] = mapped_column(primary_key=True)
    last_name: Mapped[str] = mapped_column(String(100))
    first_name: Mapped[str] = mapped_column(String(100))
    patronymic: Mapped[Optional[str]] = mapped_column(String(100))
    birthday: Mapped[str] = mapped_column(String(10))
    age: Mapped[int] = mapped_column(Integer)
    gender: Mapped[str] = mapped_column(String(10))
    pay_method: Mapped[str] = mapped_column(String(10))

    contacts: Mapped[List['Contacts']] = relationship(backref='users', cascade='all, delete-orphan', viewonly=True)

    # def __init__(self, data):
    #     super().__init__()
    #     self.data = data

    def __repr__(self) -> str:
        ...
        return f"User(id={self.id!r}, last_name={self.last_name!r}, " \
               f"first_name={self.first_name!r}, " \
               f"patronymic={self.patronymic!r}), " \
               f"birthday={self.birthday!r}), " \
               f"age={self.age!r}), " \
               f"gender={self.gender!r}), " \
               f"pay_method={self.pay_method!r}),"

    def insert_to_db(self, data):
        with Session(engine) as session:
            for line in data:
                user = Users(last_name=line['ФИО'],
                             first_name=line['ФИО'],
                             patronymic=line['ФИО'],
                             birthday=line['День рождения'],
                             age=line['Возраст'],
                             gender=line['Пол'],
                             pay_method=line['Метод оплаты'],
                             contacts=[Contacts(phone=line['Телефон'])]
                             )
                session.add(user)
            session.commit()


Base.metadata.create_all(engine)
