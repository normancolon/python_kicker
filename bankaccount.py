class BankAccount:
    def __init__(self, account_holder_name, account_number):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful. New balance: {self.balance}")
        else:
            print("Invalid amount. Please enter a positive number.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal successful. Remaining balance: {self.balance}")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        print(f"Current balance: {self.balance}")


def main():
    accounts = {}
    while True:
        print("\nWelcome to the Basic Banking System")
        print("1. Create a new account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Check account balance")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter account holder name: ")
            account_number = input("Enter account number: ")
            accounts[account_number] = BankAccount(name, account_number)
            print("Account created successfully.")
        
        elif choice == '2':
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            if account_number in accounts:
                accounts[account_number].deposit(amount)
            else:
                print("Account not found.")
        
        elif choice == '3':
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            if account_number in accounts:
                accounts[account_number].withdraw(amount)
            else:
                print("Account not found.")

        elif choice == '4':
            account_number = input("Enter account number: ")
            if account_number in accounts:
                accounts[account_number].get_balance()
            else:
                print("Account not found.")

        elif choice == '5':
            print("Thank you for using the Basic Banking System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
