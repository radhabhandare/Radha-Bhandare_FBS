#2 2. Write a program to find maximum and minimum element in a list.

li = [10, 20, 30, 40, 50]

maxli = li[0]
minli = li[0]

for i in li:
    if i > maxli:
        maxli = i

    if i < minli:
        minli = i

print(maxli)
print(minli)