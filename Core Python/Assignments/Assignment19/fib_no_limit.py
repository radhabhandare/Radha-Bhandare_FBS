def fibonacci(limit):
    a = 0
    b = 1

    while a <= limit:
        yield a
        a, b = b, a + b


n = int(input('Enter the limit: '))

for i in fibonacci(n):
    print(i, end=' ')