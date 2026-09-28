#5. Accept a number from user and check if this element is present in the list or not. Also tell how many times it is present in the list.

li = [10, 20, 30, 40, 50, 10, 20, 30, 10]

num = int(input('enter a number:'))
count = 0
for i in li:
  if i ==num:
    count +=1
if count > 0:
  print(f'The number {num} is present in the list {count} times.')
else:
  print(f'The number {num} is not present in the list.')
  


