#2. Convert temp from Celsius to Fahrenheit. (C/5 = (F-32)/9)

c = float(input("Enter temperature in Celsius: "))

f = (c * 9/5) + 32
print(f"{c} degrees Celsius is equal to {f} degrees Fahrenheit.")