# Lesson 6: Object-Oriented Programming (OOP) Basics

class BankAccount:
    """A simple class representing a bank account."""

    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount: float):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. Remaining balance: ${self.balance:.2f}")
        else:
            print("Insufficient funds or invalid amount!")

# Create an instance (object) of BankAccount
account = BankAccount("Alex", 100.0)
print(f"Account Owner: {account.owner}, Initial Balance: ${account.balance:.2f}")

account.deposit(50.0)
account.withdraw(30.0)
