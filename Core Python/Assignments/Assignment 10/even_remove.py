# 13 . Write a program to print list after removing even numbers.

li = [7, 9, 11, 2, 4, 19, 10, 20]

newli = []

for i in li:
    if i % 2 != 0:
        newli.append(i)

print(newli)