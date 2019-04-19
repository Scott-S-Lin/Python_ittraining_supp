class Demo:
    i = 100
    def hello(self):
        print('hello')

d = Demo()
print(type(Demo))
print(type(d))
print(d.i)
d.hello()
