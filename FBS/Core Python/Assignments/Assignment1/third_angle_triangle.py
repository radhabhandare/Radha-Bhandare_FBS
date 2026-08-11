#6. Write a Program to input two angles from user and find third angle of the triangle. 

angle1 = float(input('Enter first angle of triangle: '))
angle2 = float(input('Enter second angle of triangle: '))

angle3 = 180 - (angle1 + angle2)

print('Third angle of triangle: ', angle3)