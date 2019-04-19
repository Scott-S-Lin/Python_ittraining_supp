class Demo:
        x = 0
        def __init__(self,i):
                self.i = i
                Demo.x += 1
        def hello(self):
                print("hello",self.i)
                
print('There are', Demo.x,'instances.')
a = Demo(1122)
a.hello()
print('a.x = ',a.x)

b = Demo(3344)
b.hello()
print('b.x = ',b.x)

print('After all, there are',Demo.x,'instances')
