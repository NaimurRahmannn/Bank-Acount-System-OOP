from dataclasses import dataclass

@dataclass
class Customer:
    customer_id:int
    name: str
    email: str
    def __str__(self):
        return f"{self.name} | Email : {self.email}"