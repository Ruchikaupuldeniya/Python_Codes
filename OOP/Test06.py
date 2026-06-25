class Account:
    def __init__(self,account_number,balance):
        self.__account_number = account_number
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def deposit(self,amount):
        if(amount >0):
            self.__balance += amount
            print(f"Successfully deposited {amount}.New Balance:{self.__balance}")
        
        else:
            print("Deposit amount must be positive")

    def withdraw(self,amount):
        if amount>self.__balance:
            print("Insufficient Balance!")

        else:
            self.__balance -= amount
            print(f"Succeefully withdraw {amount}.Remaining Balance: {self.__balance}")

my_account =Account(123456,5000)
my_account.deposit(10000)