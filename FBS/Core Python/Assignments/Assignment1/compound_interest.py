#5. Write a program to enter P, T, R and calculate Compound Interest.
p = int(input('enter a prin amount: '))
r = float(input('enter a rate of interest: '))
t = int(input('enter a time in years: '))

Amount = p * ((1 + r / 100) **t) # p *(power(1 + r / 100, t))

ci = Amount - p
print('Compound interest ', ci)