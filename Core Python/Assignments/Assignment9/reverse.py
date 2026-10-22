def reverse(n, rev):
    if n == 0:
        return rev
    digit = n % 10
    rev = rev * 10 + digit
    return reverse(n // 10, rev)


num = int(input('Enter a number: '))
print('Reversed number:', reverse(num, 0))
