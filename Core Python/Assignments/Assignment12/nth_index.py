s = input('Enter a string: ')
n = int(input('Enter index to remove: '))

if 0 <= n < len(s):
    s = s[:n] + s[n + 1:]
    print('Result:', s)
else:
    print('Invalid index')