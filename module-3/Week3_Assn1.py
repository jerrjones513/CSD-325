class BankAccount:
    """Represents a customer's bank account."""

    def __init__(self, owner, initial_balance, pin):
        # Public attribute
        self.owner = owner

        # Private attributes
        self.__balance = initial_balance
        self.__pin = pin

    # Public method
    def deposit(self, amount):
        """Adds money to the account."""
        if self.__validate_amount(amount):
            self.__balance += amount
            print(f"${amount:.2f} deposited successfully.")

    # Public method
    def withdraw(self, amount, pin):
        """Withdraws money if the PIN and balance are valid."""
        if not self.__check_pin(pin):
            print("Incorrect PIN.")
            return

        if not self.__validate_amount(amount):
            return

        if amount > self.__balance:
            print("Insufficient funds.")
            return

        self.__balance -= amount
        print(f"${amount:.2f} withdrawn successfully.")

    # Public method
    def get_balance(self):
        """Returns the current account balance."""
        return self.__balance

    # Private method
    def __check_pin(self, pin):
        """Checks whether the supplied PIN is correct."""
        return pin == self.__pin

    # Private method
    def __validate_amount(self, amount):
        """Ensures a transaction amount is positive."""
        if amount <= 0:
            print("Amount must be greater than zero.")
            return False
        return True


class AccountPrinter:
    """Responsible only for displaying account information."""

    # Public method
    def display_account(self, account):
        print("\n--- Account Information ---")
        print(f"Owner: {account.owner}")
        print(f"Balance: ${account.get_balance():.2f}")


# -----------------------------------------
# Create class instances
# -----------------------------------------

account1 = BankAccount("Alice", 500.00, "1234")
account2 = BankAccount("Bob", 1000.00, "5678")

# Use public methods
account1.deposit(200)
account1.withdraw(100, "1234")

account2.deposit(300)
account2.withdraw(150, "5678")

# Create an instance of AccountPrinter
printer = AccountPrinter()

# Display account information
printer.display_account(account1)
printer.display_account(account2)