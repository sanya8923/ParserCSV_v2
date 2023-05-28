from base import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import engine
# from users_db import Users


class Contacts(Base):
    __tablename__ = 'contacts_table'

    id: Mapped[int] = mapped_column(primary_key=True)
    phone: Mapped[str] = mapped_column(String(15))
    user_id: Mapped[int] = mapped_column(ForeignKey('users_table.id'))

    user: Mapped['Users'] = relationship(back_populates='contacts')

    def __repr__(self) -> str:
        ...
        return f"Contacts(id={self.id!r}, phone={self.phone!r})"


Base.metadata.create_all(engine)


