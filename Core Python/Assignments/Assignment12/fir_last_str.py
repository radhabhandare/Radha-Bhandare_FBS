s = input('Enter a string: ')

if len(s) > 1:
    s = s[-1] + s[1:-1] + s[0]

print('Result:', s)