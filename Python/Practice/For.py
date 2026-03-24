#FOR
n1=int(input('num1: '))
n2=int(input('num2: '))

for p in range(n1,n2+1):
    if (p%2==0):
        print('Even Number',p)
    else:
        print('Odd Number',p)