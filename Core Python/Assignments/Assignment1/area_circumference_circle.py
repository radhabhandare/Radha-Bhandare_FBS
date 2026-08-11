#11. Find the area and circumference of circle.

r = float(input('Enter radius of circle: '))
area = 3.14 * (r ** 2)  # pi * r^2
circumference = 2 * 3.14 * r  # 2 * pi * r

print('Area of circle: ', area)
print('Circumference of circle: ', circumference)