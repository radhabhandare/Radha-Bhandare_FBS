# 12. Write a program to check if given number is Armstrong number or not.

n = int(input('Enter number: '))

temp = n
count = 0
sum = 0

while n > 0:
    count = count + 1
    n = n // 10

n = temp

while n > 0:
    digit = n % 10
    sum = sum + digit ** count
    n = n // 10

if sum == temp:
    print('Armstrong number')
else:
    print('Not an Armstrong number')