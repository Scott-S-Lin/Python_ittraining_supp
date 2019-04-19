class Demo:
	
	def __init__(self,name):
		self.name = name
	def hello(self):
		print("hello",self.name)
d = Demo("Tom")
print(help(d))
