#10. Write a program to remove all occurrences of a given element in the list.

li = [10, 20, 30, 40, 50, 10, 20, 30]
# element_remove = 10 

# for i in li:
#   if i ==element_remove:
#     li.remove(i)


# print(li)

num = int(input('enter a number to remove from the list:'))

newli = []
for i in li:
  if i != num:
    newli.append(i)
    
print(newli)