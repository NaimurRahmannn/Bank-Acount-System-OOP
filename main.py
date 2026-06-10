class Bank:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.__balance = balance
        self.transactions = []

    def deposite(self,amount):
        if amount<=0:
            print("Deposit amount must be positive")
            return
        self.__balance+=amount
    
    def withdraw(self,amount):
        if self.__balance-amount<0:
           print("Balance insufficient")
           return
        self.__balance-=amount

    def check_balance(self):
        return self.__balance  

account1=Bank("Naimur","Rahman",1000)
account1.deposite(500)
account1.withdraw(500)
#print(account1.balance)
print(account1.check_balance())