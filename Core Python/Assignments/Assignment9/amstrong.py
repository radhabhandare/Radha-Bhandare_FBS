def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)


def armstrong(n, power):
    if n == 0:
        return 0
    digit = n % 10
    return digit ** power + armstrong(n // 10, power)


num = int(input('Enter a number: '))

if num == 0:
    digits = 1
else:
    digits = count_digits(num)

if armstrong(num, digits) == num:
    print('Armstrong number')
else:
    print('Not an Armstrong number')
