l1 = float(input('Enter length of first room:'))
b1 = float(input('Enter breadth of first room:'))

l2 = float(input('Enter length of second room:'))
b2 = float(input('Enter breadth of second room:'))

height = float(input('Enter height:'))
cost = float(input('Enter cost per square meter:'))

perimeter1 = 2 * (l1 + b1)
perimeter2 = 2 * (l2 + b2)

area1 = perimeter1 * height
area2 = perimeter2 * height

totalarea = area1 + area2

totalcost = totalarea * cost

print('Total wall area :', totalarea)
print('Total cost :', totalcost)