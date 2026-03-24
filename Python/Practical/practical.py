#FIBONACCI SERIES

n=int(input("Enter your Number: "))
a=0
b=1
c=1

print(a)
print(b)

while n>0:
    c=a+b
    a=b
    b=c
    n=n-1
    print(c)
