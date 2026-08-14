# 11. WAP to check if given number Strong Number.

n = int(input('Enter number: '))

temp = n
sum = 0

while n > 0:
    digit = n % 10

    fact = 1

    for i in range(1, digit + 1):
        fact = fact * i

    sum = sum + fact
    n = n // 10

if sum == temp:
    print('Strong number')
else:
    print('Not a strong number')