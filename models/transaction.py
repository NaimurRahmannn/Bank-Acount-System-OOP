from dataclasses import dataclass

@dataclass
class Transaction:
    transaction_type:str
    account_balance:int
    note:str
    
    def __str__(self):
        return(
            f"{self.transaction_type} | "
            f"Amount: {self.account_balance} | "
            f"Note: {self.note}"
        )