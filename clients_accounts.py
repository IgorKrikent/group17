from abc import ABC, abstractmethod
import random
from typing import Self


class Client:
    def __init__(self, name: str):

        self.name = name
        self.accounts = []

    @property
    def is_positive_balance(self) -> bool:

        money = 0

        for account in self.accounts:

            money += account.balance

        if money >= 0:

            return True

        return False


class BaseAccount(ABC):
    def __init__(self):

        self.number = random.randint(100000000000, 999999999999)
        self.balance = 0

    def deposit_money(self, summa: int | float) -> None:

        if summa <= 0:

            print("\nFAILED! You must deposit some money")
            return

        self.balance += summa

    @abstractmethod
    def cash_withdrawal(self, summa: int | float) -> None:

        if summa <= 0:

            print("\nFAILED! You must withdraw some money")
            return

    @abstractmethod
    def make_transaction(self, other: Self, summa: int | float):

        pass


class CurrentAccount(BaseAccount):
    def make_transaction(self, other: BaseAccount, summa: int | float):

        if self.balance - summa < 0:

            print('Not enough money')
            return

        self.balance -= summa
        other.balance += summa

    def cash_withdrawal(self, summa: int | float) -> None:

        super().cash_withdrawal(summa=summa)

        if self.balance < summa:

            print('Not enough money')
            return

        self.balance -= summa


class CreditAccount(BaseAccount):

    percent_commission = 10 / 100

    def __init__(self, limit: int):

        super().__init__()

        self.limit = limit

    def make_transaction(self, other: BaseAccount, summa: int | float):

        take_money = summa + (summa * self.percent_commission)

        if (self.balance - take_money) < self.limit:

            print('Not enough money')
            return

        self.balance -= take_money
        other.balance += summa

    def cash_withdrawal(self, summa: int | float) -> None:

        super().cash_withdrawal(summa=summa)

        take_money = summa + (summa * self.percent_commission)

        if (self.balance - take_money) < self.limit:

            print('Not enough money')
            return

        self.balance -= take_money

