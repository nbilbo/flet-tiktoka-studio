from typing import Any, Dict, List, Optional, Type

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models import Base
from app.models import Account
from app.models import User


class DataBase:
    def __init__(self) -> None:
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        session_class = sessionmaker(self.engine)
        self.session = session_class()

    def insert_user(self, user: User) -> None:
        self.session.add(user)
        self.session.commit()

    def select_users(self) -> List[Type[User]]:
        return self.session.query(User).all()

    def select_user(self, **filter_by: Optional[Dict[str, Any]]) -> Optional[User]:
        return self.session.query(User).filter_by(**filter_by).first()

    def insert_account(self, account: Account) -> None:
        self.session.add(account)
        self.session.commit()

    def select_accounts(self, user: User) -> List[Type[Account]]:
        return self.session.query(Account).filter(Account.user == user).all()

    def select_account(self, user: User, **filter_by: Optional[Dict[str, Any]]) -> Optional[Account]:
        return self.session.query(Account).filter(Account.user == user).filter_by(**filter_by).first()

    def update_account(self, _account: Account) -> None:
        self.session.commit()

    def delete_account(self, account: Account) -> None:
        self.session.delete(account)
        self.session.commit()
