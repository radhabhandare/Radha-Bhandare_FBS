# 7 .Program to Find the Roots of a Quadratic Equation

a =int(input('Enter a: '))
b =int(input('Enter b: '))
c =int(input('Enter c: '))

d = (b**2) - (4*a*c)

root1 = (-b + d**0.5) / (2*a)
root2 = (-b - d**0.5) / (2*a)

print('Root 1: ', root1)
print('Root 2: ', root2)
