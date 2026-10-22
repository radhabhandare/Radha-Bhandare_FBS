s = input('Enter a string: ')
digits = 0
letters = 0

for ch in s:
    if ch.isdigit():
        digits += 1
    elif ch.isalpha():
        letters += 1

print('Number of digits:', digits)
print('Number of letters:', letters)