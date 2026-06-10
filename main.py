from exception import BankError
from services.bank import Bank


def main():
    bank = Bank("Python Bank")

    customer1 = bank.create_customer(
        customer_id="C1",
        name="Naimur",
        email="naimur@example.com",
        phone="0162116384"
    )

    customer2 = bank.create_customer(
        customer_id="C2",
        name="Rahman",
        email="rahman@example.com",
        phone="01854845845"
    )

    savings = bank.create_savings_account(
        account_number="S101",
        customer_id=customer1.customer_id,
        initial_balance=1000
    )

    current = bank.create_current_account(
        account_number="C101",
        customer_id=customer2.customer_id,
        initial_balance=2000
    )

    print("Initial accounts:")
    bank.show_all_accounts()

    print("\nDeposit:")
    savings.deposit(500)
    print(savings)

    print("\nWithdraw:")
    savings.withdraw(300)
    print(savings)

    print("\nAdd interest:")
    interest = savings.add_interest()
    print(f"Interest added: {interest}")
    print(savings)

    print("\nTransfer:")
    bank.transfer("S101", "CR101", 400)
    print(savings)
    print(current)

    print("\nSavings account transactions:")
    for transaction in savings:
        print(transaction)

    print("\nCurrent account transactions:")
    for transaction in current:
        print(transaction)

    print("\nTotal savings transactions:", len(savings))

    print("\nTesting current account overdraft:")
    current.withdraw(6000)
    print(current)


if __name__ == "__main__":
    try:
        main()
    except BankError as error:
        print(f"Bank error: {error}")