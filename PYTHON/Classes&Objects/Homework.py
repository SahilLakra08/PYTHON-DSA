# #create a bank class usmai account number , account name ,
# #  account balance 3 attribute h jo self. se chlenge'
# def set data
# def min balance
# min balane=0
# func def deposit(amout):
#      balance=balance+amount
#      def withdraw()
#     if self.balance<1000
# print  u cant withdrw
# else self.balance=self.balance-amount
# def display
# create customer object= class


class Bank:
    def __init__(self, account_number, account_name, balance=0):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance

    def set_data(self, account_number, account_name, balance):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Insufficient balance. You cannot withdraw this amount.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")

    def display(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Name: {self.account_name}")
        print(f"Account Balance: {self.balance}")

def menu():
    print("\n--- Bank Menu ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Display Account Details")
    print("5. Exit")

def main():
    bank_account = None

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            account_number = input("Enter account number: ")
            account_name = input("Enter account name: ")
            balance = float(input("Enter initial balance: "))
            bank_account = Bank(account_number, account_name, balance)
            print("Account created successfully!")

        elif choice == '2':
            if bank_account is None:
                print("No account found. Please create an account first.")
            else:
                amount = float(input("Enter deposit amount: "))
                bank_account.deposit(amount)

        elif choice == '3':
            if bank_account is None:
                print("No account found. Please create an account first.")
            else:
                amount = float(input("Enter withdrawal amount: "))
                bank_account.withdraw(amount)

        elif choice == '4':
            if bank_account is None:
                print("No account found. Please create an account first.")
            else:
                bank_account.display()

        elif choice == '5':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

