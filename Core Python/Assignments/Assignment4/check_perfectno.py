#10. WAP to check if given number is Perfect Number.

n = int(input('Enter number: '))

sum = 0

for i in range(1, n):
    if n % i == 0:
        sum = sum + i

if sum == n:
    print('Perfect number')
else:
    print('Not a perfect number')