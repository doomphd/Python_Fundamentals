class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance    
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance += amount
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        self.balance += self.int_rate*self.balance
        return self


class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.savings = BankAccount(0.02, 50)	# added this line
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.savings.deposit(amount)
        return self
    def make_withdrawal(self, amount):
        self.savings.withdraw(amount)	
        return self

    def display_user_balance(self):
        print(f"User: {self.name} Savings Balance: {self.savings.balance}")
        return self

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
todd = User("Todd Smith", "todd@python.com")
guido.make_deposit(100).make_deposit(200).make_deposit(200).make_withdrawal(250).display_user_balance()	
monty.make_deposit(50).make_deposit(100).make_withdrawal(20).display_user_balance()	
todd.make_deposit(3000).make_withdrawal(2176).make_withdrawal(68).make_withdrawal(230).display_user_balance()

