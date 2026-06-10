class BankError(Exception):
    pass
class InvalideAccountError(BankError):
    pass
class InsufficientBalanceError(BankError):
    pass
class AccountNotFound(BankError):
    pass