import pytest

from clients_accounts import CurrentAccount, CreditAccount, Client


@pytest.fixture(scope='class')
def current_account() -> CurrentAccount:

    instance = CurrentAccount()

    return instance


@pytest.fixture(scope='class')
def credit_account() -> CreditAccount:

    instance = CreditAccount(limit=-2000)

    return instance


@pytest.fixture(scope='class')
def client() -> Client:

    instance = Client(name='Alex')

    return instance


@pytest.fixture(scope='class')
def another_client() -> Client:

    instance = Client(name='Bob')

    return instance

