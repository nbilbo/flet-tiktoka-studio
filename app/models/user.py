from __future__ import annotations

from datetime import datetime
from typing import List
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models import Base

if TYPE_CHECKING:
    from app.models import Account


class User(Base):
    __tablename__ = 'user'

    iduser: Mapped[int] = mapped_column(init=False, primary_key=True)
    username: Mapped[str] = mapped_column(init=True, nullable=False)
    password: Mapped[str] = mapped_column(init=True, nullable=False)
    created_on: Mapped[datetime] = mapped_column(default_factory=datetime.now)
    updated_on: Mapped[datetime] = mapped_column(default_factory=datetime.now, onupdate=datetime.now)
    accounts: Mapped[List[Account]] = relationship(default_factory=list, back_populates='user')
