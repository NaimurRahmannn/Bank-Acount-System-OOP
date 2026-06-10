from exception import (
    InsufficientBalanceError,
    InvalideAccounttError
)
from models.customer import Customer
from models.transaction import Transaction


class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.__balance = balance
        self.__transactions = []

    def balance(self):
        return self.__balance

    def transaction(self):
        return self.__transactions

    def deposit(self, amount):
        if amount <= 0:
            raise InvalideAccounttError("Deposit amount needs to be positive")

        self.__balance += amount
        self.__transactions.append(f"Deposit: {amount}")
        return self.__balance

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalideAccounttError("Withdrawal amount needs to be positive")

        if amount > self.__balance:
            raise InsufficientBalanceError("Insufficient balance error")

        self.__balance -= amount
        self.__transactions.append(f"Withdraw: {amount}")
        return self.__balance

    def transfer(self, amount, receiver_account):
        if amount <= 0:
            raise InvalideAccounttError("Transfer amount needs to be positive")

        if amount > self.__balance:
            raise InsufficientBalanceError("Insufficient balance for transfer")

        self.__balance -= amount
        receiver_account.__balance += amount

        self.__transactions.append(
            f"Transfer sent: {amount} to {receiver_account.owner}"
        )
        receiver_account.__transactions.append(
            f"Transfer received: {amount} from {self.owner}"
        )

        return self.__balance

    def check_balance(self):
        return self.__balance

    def show_transactions(self):
        if not self.__transactions:
            print("No transactions yet")
            return

        for transaction in self.__transactions:
            print(transaction)

    def __str__(self):
        return f"{self.owner}'s Account | Balance: {self.__balance}"

    def __len__(self):
        return len(self.__transactions)

    def __iter__(self):
        return iter(self.__transactions)


class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner, balance=0, interest_rate=0.05):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.check_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest added: {interest}")
        return interest


class CurrentAccount(BankAccount):
    def __init__(self, account_number, owner, balance=0, overdraft_limit=5000):
        super().__init__(account_number, owner, balance)
        self.overdraft_limit = overdraft_limit
