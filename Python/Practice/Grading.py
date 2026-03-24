#GRADING
n1=int(input('Enter your Python marks'))
n2=int(input('Enter your Maths marks'))
n3=int(input('Enter your Design Thinking marks'))
n4=int(input('Enter your Computer Fundamental marks'))
p=(n1+n2+n3+n4)/400*100
if (p>=90):
    print('Grade A')
elif (p>80 and p<90):
    print('Grade B')
elif (p>70 and p<=80):
    print('Grade C')
elif (p>60 and p<=70):
    print('Grade D')
else:
    (p<60)
    print('Out of competition')
