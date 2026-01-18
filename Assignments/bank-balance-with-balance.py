# Taking Inputs
name = input()
balance = float(input())

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def ShowBalance(self):
        return f"Name: {self.name}, Balance: {self.balance}"
        


# Create object and print result
account = BankAccount(name, balance)
print(account.ShowBalance())