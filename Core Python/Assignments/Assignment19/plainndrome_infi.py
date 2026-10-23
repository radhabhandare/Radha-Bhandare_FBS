def palindrome():
    n = 0

    while True:
        if str(n) == str(n)[::-1]:
            yield n
        n = n + 1


g = palindrome()

for i in range(10):
    print(next(g))