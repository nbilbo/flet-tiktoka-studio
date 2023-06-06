from typing import Generator

from factory import Factory
from faker import Faker
from pytest import fixture
from pytest import mark

from app.models import Account
from app.models import DataBase
from app.models import User


class UserFactory(Factory):
    class Meta:
        model = User

    username = Faker().name()
    password = Faker().password()


class AccountFactory(Factory):
    class Meta:
        model = Account

    email = Faker().email()
    password = Faker().password()


@fixture(scope='function')
def empty_database() -> Generator[DataBase, None, None]:
    database = DataBase()
    yield database


def test_insert_user_must_set_iduser_to_inserted_user(empty_database) -> None:
    user = UserFactory.build()
    empty_database.insert_user(user)
    assert user.iduser is not None


def test_insert_user_must_set_created_on_to_inserted_user(empty_database) -> None:
    user = UserFactory.build()
    empty_database.insert_user(user)
    assert user.created_on is not None


def test_insert_user_must_set_updated_on_to_inserted_user(empty_database) -> None:
    user = UserFactory.build()
    empty_database.insert_user(user)
    assert user.updated_on is not None


@mark.parametrize('count_users', (1, 10))
def test_select_users_must_return_users_list(empty_database, count_users: int) -> None:
    for count in range(count_users):
        user = UserFactory.build()
        empty_database.insert_user(user)

    assert len(empty_database.select_users()) == count_users


def test_select_user_must_return_single_user(empty_database) -> None:
    user = UserFactory.build()
    empty_database.insert_user(user)
    assert empty_database.select_user(username=user.username) is not None


def test_insert_account_must_set_idaccount_to_inserted_account(empty_database) -> None:
    account = AccountFactory.build()
    account.user = UserFactory.build()
    empty_database.insert_account(account)
    assert account.idaccount is not None


def test_update_account_must_persist_data(empty_database) -> None:
    user = UserFactory.build()
    user.accounts = [AccountFactory()]
    empty_database.insert_user(user)

    account = user.accounts[0]
    account.email = Faker().email()
    empty_database.update_account(account)

    register = empty_database.select_account(user, email=account.email)
    assert register.email == account.email


def test_delete_account_must_persist_data(empty_database) -> None:
    user = UserFactory.build()
    user.accounts = [AccountFactory.build()]
    empty_database.insert_user(user)
    empty_database.delete_account(user.accounts[0])
    assert len(user.accounts) == 0
