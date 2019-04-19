n = int(input())
W=1
h = n - 1 # 帽高
for i in range(0,h+1) :
    if(i==0):
        print(' '*(h-i),'*',sep='')
    elif(i==h):
        print(' '*(h-i),'/',sep='',end='')
        print('-'*W,end='')
        print('\\')
    else:
        print(' '*(h-i),'/',sep='',end='')
        print('.'*W,end='')
        W +=2 #帽寬
        print('\\')

