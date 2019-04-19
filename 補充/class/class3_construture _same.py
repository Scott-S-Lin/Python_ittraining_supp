class Demo:
        i = 0
        def __init__(self,i):
                self.i = i
                Demo.i += 1
        def hello(self):
                print("hello",self.i)
                
print('There are', Demo.i,'instances.')
a = Demo(1122)
a.hello()
print('a.i = ',a.i)

b = Demo(3344)
b.hello()
print('b.i = ',b.i)

print('After all, there are',Demo.i,'instances')
