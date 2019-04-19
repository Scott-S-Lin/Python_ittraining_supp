n = int(input())
W=0
h = n - 1 # 山高
for i in range(0,h+1) :
        print(' '*(h-i),'/',sep='',end='') 
        if(i==1):
            W +=2 #山寬
            print('~'*W,end='')
        elif(W!=0 and i>0):
            W +=2 #山寬
            print(' '*W,end='')
        print('\\')
print('~'*(W+2))
print('~'*(W+2))
