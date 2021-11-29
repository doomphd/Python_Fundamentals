class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)	# added this line
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)	
        return self

    def display_user_balance(self):
        print(f"{self.account}")
        return self

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
todd = User("Todd Smith", "todd@python.com")
guido.make_deposit(100).make_deposit(200).make_deposit(200).make_withdrawal(250).display_user_balance()	
monty.make_deposit(50).make_deposit(100).make_withdrawal(20).display_user_balance()	
todd.make_deposit(3000).make_withdrawal(2176).make_withdrawal(68).make_withdrawal(235).display_user_balance()
