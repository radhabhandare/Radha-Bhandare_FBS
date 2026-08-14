# 6. Write a program to print first n prime numbers.

n = int(input('Enter n : '))

num = 2
count = 0

while count < n:

    factors = 0

    for i in range(1, num + 1):

        if num % i == 0:
            factors = factors + 1

    if factors == 2:
        print('Prime Number :', num)
        count = count + 1

    num = num + 1