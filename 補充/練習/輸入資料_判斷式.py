
while True:
    n=input()
    sumf=1
    sumw=1
    if n=='q':
            break 

if str(type(n))=="<class'float'>":
    sumf = sumf*n
    print(sumf*n)

if str(type(n))=="<class'int'>":
    sumw = sumw*n
    print(sumw*n)
        
if sumf > sumw:
    print('Float>Int')
if sumf == sumw:
    print('Float=Int')
if sumf < sumw:
    print('Float<Int')

       

