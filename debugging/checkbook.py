class Checkbook:
    def __init__(self):
        # Initialize the balance to 0.0 when a Checkbook object is created
        self.balance = 0.0

    def deposit(self, amount):
        # Increase the balance by the deposited amount
        self.balance += amount
        # Print a message indicating the deposit amount and current balance
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        # Check if the withdrawal amount is greater than the current balance
        if amount > self.balance:
            # Print a message if there are insufficient funds
            print("Insufficient funds to complete the withdrawal.")
        else:
            # Subtract the withdrawal amount from the balance
            self.balance -= amount
            # Print a message indicating the withdrawal amount and current balance
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        # Print the current balance
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    # Create a Checkbook object
    cb = Checkbook()
    while True:
        # Ask the user for their action (deposit, withdraw, balance, or exit)
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            # Exit the loop if the user wants to exit
            break
        elif action.lower() == 'deposit':
            # Ask the user for the amount to deposit and call the deposit method
            amount = float(input("Enter the amount to deposit: $"))
            cb.deposit(amount)
        elif action.lower() == 'withdraw':
            # Ask the user for the amount to withdraw and call the withdraw method
            amount = float(input("Enter the amount to withdraw: $"))
            cb.withdraw(amount)
        elif action.lower() == 'balance':
            # Call the get_balance method to display the current balance
            cb.get_balance()
        else:
            # Print a message if the user enters an invalid command
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    # Call the main function if the script is executed directly
    main()
