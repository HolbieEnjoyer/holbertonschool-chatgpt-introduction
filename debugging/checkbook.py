class Checkbook:
    def __init__(self):
        """
        Initialize the Checkbook object with a balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit the specified amount into the checkbook balance.

        Args:
            amount (float): The amount to deposit.

        Returns:
            None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw the specified amount from the checkbook balance.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Retrieve the current balance of the checkbook.

        Returns:
            None
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Main function to interact with the Checkbook object.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            amount = get_valid_amount("Enter the amount to deposit: $")
            cb.deposit(amount)
        elif action.lower() == 'withdraw':
            amount = get_valid_amount("Enter the amount to withdraw: $")
            cb.withdraw(amount)
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

def get_valid_amount(prompt):
    """
    Prompt the user for a numeric amount until a valid input is provided.

    Args:
        prompt (str): The prompt message to display to the user.

    Returns:
        float: The valid numeric amount entered by the user.
    """
    while True:
        try:
            amount = float(input(prompt))
            return amount
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")

if __name__ == "__main__":
    main()
