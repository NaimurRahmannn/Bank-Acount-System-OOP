class BankError(Exception):
    pass
class InvalideAccounttError(BankError):
    pass
class InsufficientBalanceError(BankError):
    pass
class AccountNotFoundError(BankError):
    pass