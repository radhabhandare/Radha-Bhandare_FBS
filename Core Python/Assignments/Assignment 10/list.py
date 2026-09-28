# 12. Write a program to create three lists of numbers, their squares and cubes

li = [1, 2, 3, 4, 5]

square = []
cube = []

for i in li:
    square.append(i * i)
    cube.append(i*i*i)

print('Numbers ', li)
print('Squares ', square)
print('Cubes ', cube)