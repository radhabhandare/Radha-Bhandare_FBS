def memoize(func):
    cache = {}

    def inner(n):
        if n in cache:
            print('Result from cache')
            return cache[n]

        result = func(n)
        cache[n] = result
        return result

    return inner


@memoize
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
print(factorial(5))