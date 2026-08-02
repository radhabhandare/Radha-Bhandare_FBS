#9. Write a program to enter base and height of a triangle and find its area.
base = float(input('Enter base of triangle: '))
height = float(input('Enter height of triangle: '))

area = (base * height) / 2  # 0.5 * base * height
print('Area of triangle: ', area)