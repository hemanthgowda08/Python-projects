class Account():
    def __init__(self, bal, acc):
        # Here we initialize account with balance and account number
        self.balance = bal
        self.account = acc

    def debit(self, amount):
        # Now we subtract amount from balance
        self.balance -= amount
        print("Rs.", amount, "was debited from your Account")
        print("Total balance in your account is:", self.balance)

    def credit(self, amount):
        # nWe Add amount to balance
        self.balance += amount
        print("Rs.", amount, "was credited into your Account")
        print("Total balance in your account is:", self.balance)

    def get_balance(self):
        # Return the current balance
        return self.balance

# Create an account with initial balane of 10000 and with account number 1234
acc1 = Account(10000, 1234)

acc1.debit(1000)    
acc1.credit(1090)     

# Print final balance
print("Final balance is:", acc1.get_balance())
