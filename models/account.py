class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.__balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive")
            return
        self.__balance += amount
        self.transactions.append(f"Deposit: {amount}")

    def withdraw(self, amount):
        if self.__balance - amount < 0:
            print("Balance insufficient")
            return
        self.__balance -= amount
        self.transactions.append(f"Withdraw: {amount}")

    def check_balance(self):
        return self.__balance

    def __str__(self):
        return f"{self.owner}'s Account | Balance: {self.__balance}"

    def __len__(self):
        return len(self.transactions)

    def __iter__(self):
        return iter(self.transactions)

class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner, balance=0, interest_rate=0.05):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.check_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest added: {interest}")
        
class CurrentAccount(BankAccount):
    def __init__(self, account_number, owner, balance=0, overdraft_limit=5000):
        super().__init__(account_number, owner, balance)
        self.overdraft_limit = overdraft_limit

savings = SavingsAccount("S101", "Naimur", 1000)
current = CurrentAccount("C101", "Rahman", 2000)


savings.deposit(500)
savings.withdraw(300)
savings.add_interest()

current.deposit(1000)
current.withdraw(500)

print(savings)
print(current)

print("Savings transactions:")
for transaction in savings:
    print(transaction)

print("Current transactions:")
for transaction in current:
    print(transaction)