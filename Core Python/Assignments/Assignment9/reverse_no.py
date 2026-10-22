def reverse(n):
    if n < 10:
        return n
    digits = len(str(n))
    return (n % 10) * (10 ** (digits - 1)) + reverse(n // 10)


n = int(input('Enter a number: '))
print('Reversed number:', reverse(n))