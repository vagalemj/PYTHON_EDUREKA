class BankAccount:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.is_locked = False
        self.lock_attempts = 0

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrawn {amount}. New balance: {self.balance}"
        else:
            return "Insufficient funds."

    def is_pin_correct(self, pin):
        if self.is_locked:
            return False

        if self.pin == pin:
            self.lock_attempts = 0
            return True
        else:
            self.lock_attempts += 1
            if self.lock_attempts >= 3:
                self.is_locked = True
            return False


def create_account(accounts):
    account_number = input("Enter a new account number: ")
    while account_number in accounts:
        print("Account number already exists. Please choose a different number.")
        account_number = input("Enter a new account number: ")

    pin = input("Create a 4-digit PIN: ")
    while len(pin) != 4 or not pin.isdigit():
        print("Invalid PIN. Please enter a 4-digit numeric PIN.")
        pin = input("Create a 4-digit PIN: ")

    initial_balance = float(input("Enter the initial balance: "))
    new_account = BankAccount(account_number, pin, initial_balance)
    accounts[account_number] = new_account
    print("Account created successfully!")


def transfer_funds(sender, recipient, amount):
    if sender.balance >= amount:
        sender.balance -= amount
        recipient.balance += amount
        return f"Transferred {amount} to account number {recipient.account_number}. " \
               f"Your new balance: {sender.balance}"
    else:
        return "Insufficient funds for transfer."


def main():
    accounts = {
        '123456789': BankAccount('123456789', '1234', 1000),
        '987654321': BankAccount('987654321', '4321', 500),
    }

    while True:
        print("\n1. Login")
        print("2. Create Account")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            account_number = input("Enter your account number: ")
            pin = input("Enter your PIN: ")

            if account_number in accounts:
                account = accounts[account_number]

                if account.is_pin_correct(pin):
                    print("Login successful.")
                else:
                    print("Account locked due to multiple incorrect PIN attempts. "
                          "Please contact customer support.")
                    break
            else:
                print("Invalid account number. Please try again.")
        elif choice == '2':
            create_account(accounts)
        elif choice == '3':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        while choice == '1':
            print("\n1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transfer Funds")
            print("5. Logout")
            option = input("Enter your choice (1/2/3/4/5): ")

            if option == '1':
                print(f"Your account balance is: {account.check_balance()}")
            elif option == '2':
                amount = float(input("Enter the amount to deposit: "))
                print(account.deposit(amount))
            elif option == '3':
                amount = float(input("Enter the amount to withdraw: "))
                print(account.withdraw(amount))
            elif option == '4':
                recipient_account = input("Enter the recipient's account number: ")
                if recipient_account in accounts and recipient_account != account.account_number:
                    amount = float(input("Enter the amount to transfer: "))
                    print(transfer_funds(account, accounts[recipient_account], amount))
                else:
                    print("Invalid recipient account number.")
            elif option == '5':
                print("Logged out.")
                break
            else:
                print("Invalid choice. Please try again.")
                
if __name__ == "__main__":
    main()