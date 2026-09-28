# 7. Write a program to create a new list from existing list which contains cube of each number of list.

li = [1, 2, 3, 4, 5]

newli =[]

for i in li:
  newli.append(i**3)
  
print(newli)