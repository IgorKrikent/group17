import random
from copy import copy

from clients_accounts import CurrentAccount, CreditAccount


class TestDepositFunds:
    def test_add_account_to_client(self, client, current_account):

        client.accounts.append(current_account)

        assert client.accounts

    def test_add_credit_account(self, client, credit_account):

        client.accounts.append(credit_account)

        assert len(client.accounts) == 2

        # print(client.accounts)

        random.shuffle(client.accounts)

    def test_deposit_on_current_on_1560(self, client):

        for account in client.accounts:

            if isinstance(account, CurrentAccount):

                account.deposit_money(1560)

                assert account.balance == 1560

                break

    def test_transfer_from_credit_to_debit(self, client):

        for account in client.accounts:

            if isinstance(account, CurrentAccount):

                current_account = account

            else:
                credit_account = account


        credit_account.make_transaction(current_account, 500)

        assert current_account.balance == 2060
        assert credit_account.balance == (-500 - (500 * CreditAccount.percent_commission))

    def test_failed_from_current_account(self, current_account, credit_account):

        # print(current_account.__dict__)

        balance_before = current_account.balance

        current_account.make_transaction(credit_account, 50000000000)

        assert current_account.balance == balance_before


class TestMoreClients:

    def test_transaction_to_other_client(self, client, another_client,
                                         current_account,
                                         credit_account):

        other_current_account = copy(current_account)
        other_credit_account = copy(credit_account)

        second_client_current_account = copy(current_account)

        client.accounts.append(current_account)
        client.accounts.append(credit_account)
        client.accounts.append(other_current_account)
        client.accounts.append(other_credit_account)

        another_client.accounts.append(second_client_current_account)

        credit_account.make_transaction(second_client_current_account, 1.33)

        assert credit_account.balance == -1.33 - 1.33 * credit_account.percent_commission
        assert second_client_current_account.balance == 1.33

