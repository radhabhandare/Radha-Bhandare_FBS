#3. Write a program to find the second largest element in the list.

li = [10, 20, 30, 40, 50]

maxli=li[0]
secondmaxli=li[0]

for i in li:
  if i > maxli:
    secondmaxli=maxli
    maxli=i
    
  elif i > secondmaxli and i != maxli:
    secondmaxli=i
    
print(secondmaxli)
