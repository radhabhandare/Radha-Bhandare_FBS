#1. Write a program to print first n prime numbers

# n = int(input('Enter a number:'))
# count = 0
# num = 2

# while count < n:
#   i = 1
#   factor = 0
  
#   while i <= num:
#     if num % i == 0:
#       factor = factor + 1
#     i = i +1
    
#     if factor == 2:
#       print(num, end= ' ')
#       count = count+1
#     num = num +1

n = int(input('Enter a number:'))
count = 0
number = 2

while count < n:
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
      break
  if is_prime:
    print(number, end=' ')
    count += 1
  number += 1