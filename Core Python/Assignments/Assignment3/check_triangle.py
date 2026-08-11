# 5. Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.
a = int(input('Enter first side: '))
b = int(input('Enter second side: '))
c = int(input('Enter third side: '))

if a == b and b == c:
    print('Equilateral triangle') #Any two sides equal
elif a == b or b == c or a == c:
    print('Isosceles triangle')  #All sides different
else:
    print('Scalene triangle')