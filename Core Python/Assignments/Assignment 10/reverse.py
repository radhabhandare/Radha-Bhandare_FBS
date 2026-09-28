# 4. Write a program to reverse the list.

li = [10, 20, 30, 40, 50]

reverse_li = []
for i in range(len(li)-1, -1, -1):
    reverse_li.append(li[i])

print(reverse_li)