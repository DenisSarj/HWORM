from typing import TYPE_CHECKING
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.Book import Book
from models.Base import Base

if TYPE_CHECKING:
    from .Book import Book

class Publisher(Base):
    __tablename__ = 'Publishers'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(60), unique=True)

    books: Mapped[list['Book']] = relationship(
        back_populates='publisher',
        cascade='all, delete-orphan',
    )
