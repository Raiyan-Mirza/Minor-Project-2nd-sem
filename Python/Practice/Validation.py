#VALIDATION
name=input("Enter your Username: ")

if len(name) > 12:
    print("Username can't exceed 12 characters.")

elif not name.isalpha:
    print("Username can't contain space and digits.")

else:
    Name= name.upper()
    print(Name)