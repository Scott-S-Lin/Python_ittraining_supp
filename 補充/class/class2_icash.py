class Account:
	def __init__ (self, initial):
		self.balance = initial
	def deposit (self, amt):
		self.balance = self.balance + amt
	def withdraw (self,amt):
		self.balance = self.balance - amt
	def getbalance (self):
		return self.balance

a = Account(1000.00)
print(a.getbalance())
a.deposit(550.23)
print(a.getbalance())
a.deposit(100)
print(a.getbalance())
a.withdraw(50)
print(a.getbalance())
