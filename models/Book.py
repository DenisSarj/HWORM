from typing import TYPE_CHECKING
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.Base import Base

if TYPE_CHECKING:
    from .Publisher import Publisher

class Book(Base):
    __tablename__ = 'books'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String[50])

    publisher_id: Mapped[int] = mapped_column(ForeignKey('publishers.id'))
    publisher: Mapped['Publisher'] = relationship(back_populates='books')
