class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        print(f"\nAccount {self.account_number} created successfully.")
        print(f"Initial Balance: {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount.")
        else:
            self.balance += amount
            print(f"Deposited Amount: {amount}")
            print(f"Updated Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Err: Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrawn Amount: {amount}")
            print(f"Updated Balance: {self.balance}")

    def __del__(self):
        print(f"\nAccount {self.account_number} is being closed.")


def main():
    print("=== Bank Account System ===")

    acc_no = input("Enter Account Number: ")
    balance = int(input("Enter Initial Balance: "))

    account = BankAccount(acc_no, balance)

    deposit_amt = int(input("\nEnter amount to deposit: "))
    account.deposit(deposit_amt)

    withdraw_amt = int(input("\nEnter amount to withdraw: "))
    account.withdraw(withdraw_amt)


if __name__ == "__main__":
    main()
