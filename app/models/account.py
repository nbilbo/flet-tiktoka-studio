from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models import Base

if TYPE_CHECKING:
    from app.models import User


class Account(Base):
    __tablename__ = 'account'

    idaccount: Mapped[int] = mapped_column(init=False, primary_key=True)
    email: Mapped[str] = mapped_column(init=True, nullable=False)
    password: Mapped[str] = mapped_column(init=True, nullable=False)
    created_on: Mapped[datetime] = mapped_column(init=False, default_factory=datetime.now)
    updated_on: Mapped[datetime] = mapped_column(init=False, default_factory=datetime.now, onupdate=datetime.now)
    id_user: Mapped[int] = mapped_column(ForeignKey('user.iduser'), default=None)
    user: Mapped[User] = relationship(init=False, default=None)
