l = float(input('Enter length  : '))
w = float(input('Enter width : '))
r = float(input('Enter radius : '))

area = l * w +(3.14 * r * r)/ 2

perimeter = 2 * (l + w) + 3.14 * r

print('Area:', area)
print('Perimeter:', perimeter)