from exception import AccountNotFoundError
from models.account import SavingsAccount, CurrentAccount
from models.customer import Customer


class Bank:
    def __init__(self, name: str):
        self.name = name
        self.customers = {}
        self.accounts = {}

    def create_customer(self, customer_id: str, name: str, email: str, phone: str):
        customer = Customer(
            customer_id=customer_id,
            name=name,
            email=email
        )

        self.customers[customer_id] = customer
        return customer

    def create_savings_account(
        self,
        account_number: str,
        customer_id: str,
        initial_balance: float = 0
    ):
        customer = self.customers[customer_id]

        account = SavingsAccount(
            account_number=account_number,
            owner=customer,
            balance=initial_balance
        )

        self.accounts[account_number] = account
        return account

    def create_current_account(
        self,
        account_number: str,
        customer_id: str,
        initial_balance: float = 0
    ):
        customer = self.customers[customer_id]

        account = CurrentAccount(
            account_number=account_number,
            owner=customer,
            balance=initial_balance
        )

        self.accounts[account_number] = account
        return account

    def get_account(self, account_number: str):
        if account_number not in self.accounts:
            raise AccountNotFoundError("Account not found")

        return self.accounts[account_number]

    def transfer(self, from_account_number: str, to_account_number: str, amount: float):
        sender = self.get_account(from_account_number)
        receiver = self.get_account(to_account_number)

        sender.transfer(amount, receiver)

    def show_all_accounts(self):
        if not self.accounts:
            print("No accounts available")
            return

        for account in self.accounts.values():
            print(account)