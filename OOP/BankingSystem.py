class Customer:
    def __init__(self, customerID, name, email):
        self.customerID = customerID
        self.name = name
        self.email = email


class Account:
    def __init__(self, accountNumber, balance=0):
        self.accountNumber = accountNumber
        self.__balance = balance  # private variable

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Successfully deposited {amount}. New Balance: {self.__balance}"
        return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient balance."
        self.__balance -= amount
        return f"Successfully withdrawn {amount}. Remaining Balance: {self.__balance}"


class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = {}
        self.accounts = {}

    def add_customer(self, customerID, name, email):
        if customerID in self.customers:
            return "Customer already exists."

        new_customer = Customer(customerID, name, email)
        self.customers[customerID] = new_customer
        return f"Customer {name} added successfully."

    def open_account(self, customerID, accountNumber):
        if customerID not in self.customers:
            return "Customer not found."

        if accountNumber in self.accounts:
            return "Account already exists."

        new_account = Account(accountNumber)
        self.accounts[accountNumber] = new_account

        customer_name = self.customers[customerID].name
        return f"Account {accountNumber} opened for {customer_name}."

    def deposit_to_acc(self, accountNumber, amount):
        if accountNumber in self.accounts:
            return self.accounts[accountNumber].deposit(amount)
        return "Account not found."

    def withdraw_from_acc(self, accountNumber, amount):
        if accountNumber in self.accounts:
            return self.accounts[accountNumber].withdraw(amount)
        return "Account not found."

    def check_balance(self, accountNumber):
        if accountNumber in self.accounts:
            return self.accounts[accountNumber].get_balance()
        return "Account not found."



#  TEST / MAIN PROGRAM


bank = Bank("My Bank")

print(bank.add_customer(1, "Nimal", "nimal@gmail.com"))

print(bank.open_account(1, 1001))

print(bank.deposit_to_acc(1001, 1000))
print(bank.withdraw_from_acc(1001, 300))

print("Final Balance:", bank.check_balance(1001))