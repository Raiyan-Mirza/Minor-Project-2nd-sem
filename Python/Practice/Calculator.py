#CALCULATOR
print("This calculator can add,subtract,multiply and divide.")
o=input("Enter you operation amoung +,-,*,/ : ")
n1=float(input("Enter your first number: "))
n2=float(input("Enter your second number: "))

if o ==("+"):
    print(n1 + n2)

elif o==("-"):
    print(n1 - n2)

elif o==("*"):
    print(n1 * n2)

elif o==("/"):
    print(n1/n2)
    
else:
    print("INVALID INPUT")

print("Thank You for using the CALCULATOR.")