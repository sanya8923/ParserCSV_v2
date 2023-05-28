from base import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, Optional


class Users(Base):
    __tablename__ = 'users_table'

    id: Mapped[int] = mapped_column(primary_key=True)
    last_name: Mapped[str] = mapped_column(String(30))
    first_name: Mapped[str] = mapped_column(String(30))
    patronymic: Mapped[Optional[str]]
    birthday: Mapped[str] = mapped_column(String(10))
    age: Mapped[str] = mapped_column(String(3))
    gender: Mapped[str] = mapped_column(String(10))
    pay_method: Mapped[str] = mapped_column(String(10))

    contacts: Mapped[List['Contacts']] = relationship(back_populates='users', cascade='all, delete-orphan')
