class InsufficientBalanceException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
            self.deficit = args[1]
        else:
            self.message = None
            self.deficit = 0.0

    def __str__(self):
        return f"InsufficientBalanceException( reason: {self.message}, deficit: {self.deficit})"


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

    # destructor
    def __del__(self):
        # deallocate the resource: close file
        print("Account's destructor is working...")
        pass

    def deposit(self, amount=10):
        if amount <= 0:  # validation
            raise ValueError(f"{amount} must be positive!")
        self.balance += amount

    def withdraw(self, amount=10, withdrawAvailable=False):
        """
        Withdraws money
        :param amount: withdraw amount
        :return: withdrawn amount
        """
        if amount <= 0:  # validation
            raise ValueError(f"{amount} must be positive!")
        if amount > self.balance:
            if withdrawAvailable:
                available = self.balance
                self.balance = 0
                return available
            else:
                message = f"Your balance ({self.balance}) does not cover your expenses({amount})"
                deficit = amount - self.balance
                raise InsufficientBalanceException(message, deficit)
        else:
            self.balance -= amount
            return amount

    def __str__(self):
        return f"Account( 'iban': {self.iban}, 'balance': {self.balance})"


# (1) Class/Object
# (2) Inheritance
# Account         -> super class, base class
# CheckingAccount -> sub class, derived class
# CheckingAccount: Account (2) -> iban, balance , CheckingAccount (1) -> overdraft_amount
class CheckingAccount(Account):
    # constructor
    def __init__(self, iban, balance=10, overdraft_amount=100):
        super().__init__(iban, balance)
        self.overdraft_amount = overdraft_amount
        # allocates a resource: open file

    # destructor
    def __del__(self):
        # deallocate the resource: close file
        print("CheckingAccount's destructor is working...")
        pass

    def withdraw(self, amount=10, withdrawAvailable=False):
        if amount <= 0:  # validation
            raise ValueError(f"{amount} must be positive!")
        elif amount > (self.balance + self.overdraft_amount):
            if withdrawAvailable:
                available = self.balance + self.overdraft_amount
                if not available:
                    message = f"Your balance ({self.balance}) does not cover your expenses({amount})"
                    deficit = amount - self.balance - self.overdraft_amount
                    raise InsufficientBalanceException(message, deficit)
                self.balance = 0.0
                return available
            else:
                message = f"Your balance ({self.balance}) does not cover your expenses({amount})"
                deficit = amount - self.balance - self.overdraft_amount
                raise InsufficientBalanceException(message, deficit)
        else:
            self.balance -= amount
            return amount


try:
    acc1 = Account(iban="tr1", balance=1_000_000)
    # del acc1 # triggers the destructor
    acc1 = CheckingAccount(iban="TR3")
    acc2 = CheckingAccount(iban="TR2", balance=50_000, overdraft_amount=10_000)
    print(acc1.withdraw(75_000))
    print(acc1.withdraw(amount=1_250_000, withdrawAvailable=True))
    print(f"{acc1.iban}: {acc1.balance}")
    print(acc1)  # Account::__str__
    print(acc2)
    print(acc2.withdraw(amount=60_000, withdrawAvailable=False))
    print(acc2)
    # print(acc2.withdraw(amount=1, withdrawAvailable=True))
except ValueError as err:
    print(err)
except InsufficientBalanceException as err:
    print(err)
