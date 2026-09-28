#Write a program to create a duplicate of an existing list. It should not point to same list.

li = [7, 9, 11, 2, 4]

newli = []

for i in li:
    newli.append(i)

print('Original list =', li)
print('Duplicate list =', newli)

newli.append(20)

print('After changing duplicate list')
print('Original list =', li)
print('Duplicate list =', newli)