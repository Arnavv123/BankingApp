from typing import List


class Banking:
    def __init__(self, acc_no, name, account_type, branch):
        self.acc_no = acc_no
        self.name = name
        self.account_type = account_type
        self.balance = 0
        self.branch = branch

    def get_balance(self) -> int:
        return self.balance

    def deposit(self, amount: int):
        self.balance += amount
        print(f"Updated balance = {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficent balance")
        else:
            self.balance -= amount
            print(f"Updated balance = {self.balance}\n\n")

    def display(self):
        print(f"Acc_no = {self.acc_no}")
        print(f"Name = {self.name}")
        print(f"Account_type = {self.account_type}")
        print(f"balance = {self.balance}")
        print(f"branch = {self.branch}\n\n")


bank_details: List[Banking] = []

while True:
    print("1. Add Account")
    print("2. Display Account")
    print("3. Check balance of account")
    print("4. Deposit balance")
    print("5. Withdraw money")
    print("6. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        acc_no = int(input("Enter account number = "))
        name = input("Enter name = ")
        account_type = input("Enter account type(saving/current) = ")
        # balance = 0
        branch = input("Enter your branch = ")

        x = Banking(acc_no, name, account_type, branch)
        bank_details.append(x)

    elif choice == 2:
        if len(bank_details) == 0:
            print("No students found")
        else:
            for b in bank_details:
                b.display()

    elif choice == 3:
        acc_n = int(input("Enter account number = "))
        for b in bank_details:
            if b.acc_no == acc_n:
                print(f"Your account balance is {b.get_balance()}")

    elif choice == 4:
        acc_n = int(input("Enter account number = "))
        for b in bank_details:
            if b.acc_no == acc_n:
                amount = int(input("Enter amount to deposit = "))
                b.deposit(amount)
                # print(f"Your account balance is {b.get_balance()}")
                break

    elif choice == 5:
        acc_n = int(input("Enter account number = "))
        for b in bank_details:
            if b.acc_no == acc_n:
                amount = int(input("Enter amount to withdraw = "))
                b.withdraw(amount)
                break

    elif choice == 6:
        break
    else:
        print("Invalid Choice")
