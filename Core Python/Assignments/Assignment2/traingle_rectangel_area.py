#WAP to calculate area of triangle and rectangle
base = float(input('Enter base of triangle: '))
height = float(input('Enter height of triangle: '))

triangle_area = 0.5 * base * height

length = float(input('Enter length of rectangle: '))
width = float(input('Enter width of rectangle: '))

rectangle_area = length * width

print('Area of Triangle ',  triangle_area)
print('Area of Rectangle ', rectangle_area)
