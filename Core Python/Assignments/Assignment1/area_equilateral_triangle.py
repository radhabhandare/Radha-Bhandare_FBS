#10. Write a program to calculate area of an equilateral triangle.

side = float(input('Enter side of equilateral triangle: '))

area = (3 ** 0.5 / 4) * (side ** 2)  # (sqrt(3)/4) * side^2 
print('Area of equilateral triangle: ', area)