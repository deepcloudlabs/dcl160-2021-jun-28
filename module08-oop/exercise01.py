class InsufficientBalanceException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
            self.deficit = args[1]
        else:
            self.message = None
            self.deficit = 0.0


class Account:
    # constructor -> python
    def __init__(self, iban, balance=0.0):
        """
        creates an account object
        :param iban: uniquely identifies the account object
        :param balance: stores amount of money
        """
        # attributes
        self.iban = iban
        self.balance = balance

    def deposit(self, amount=10):
        if amount <= 0:  # validation
            raise ValueError(f"{amount} must be positive!")
        self.balance += amount

    def withdraw(self, amount=10):
        if amount <= 0:  # validation
            raise ValueError(f"{amount} must be positive!")
        if amount > self.balance:
            message = f"Your balance ({self.balance}) does not cover your expenses({amount})"
            deficit = amount - self.balance
            raise InsufficientBalanceException(message, deficit)
        self.balance -= amount


try:
    acc1 = Account(iban="tr1", balance=1_000_000)
    acc1.withdraw(75_000)
    acc1.withdraw(125_000)
    print(f"{acc1.iban}: {acc1.balance}")
except ValueError as err:
    print(err)
except InsufficientBalanceException as err:
    print(err)