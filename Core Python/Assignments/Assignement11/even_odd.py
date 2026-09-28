#1. Python Program to Put Even and Odd elements of a List into two Different Lists
li = [10, 20 ,3, 5,12, 4, 78 ]
even = []
odd = []

for i in li:
  if i % 2 == 0:
    even.append(i)
    
  else:
    odd.append(i)
    
print('Even', even)
print('Odd', odd)