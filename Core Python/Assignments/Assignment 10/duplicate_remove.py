#6. Write a program to remove duplicates from the list.

li = [10, 20, 30, 40, 50, 10, 20, 30]

newli = []

for i in li:
  if i not in newli:
    newli.append(i)
print(newli)
