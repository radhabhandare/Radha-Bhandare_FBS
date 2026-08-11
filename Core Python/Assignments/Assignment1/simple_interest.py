#4. Write a program to enter P, T, R and calculate simple Interest.
p = int(input('enter a prin amount: '))
R = float(input('enter a rate of interest: '))
T = int(input('enter a time in years: '))

SI= (p*R*T)/100

print('simple interest ', SI)