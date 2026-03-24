#TEMPERATURE CONVERTER
print("This is a Celsius-Kelvin and Kelvin-Celcius Converter")
print("------------------------------------------------------------------------------------------------")

o=input("C-K or K-C: ")

if o ==("C-K"):
    C=float(input("Enter you temerature in celsius: "))
    Rc=(C + 273.5)
    print(f"Your temperature is {Rc}K.")

elif o ==("K-C"):
    K=float(input("Enter your tempertaure: "))
    Rk=(K -273.5)
    print(f"Your temperature is {Rk}°.")

else:
    print("INVALID OUTPUT")

print("THANK YOU FOR USING THIS TEMPERATURE CONVERTER.")