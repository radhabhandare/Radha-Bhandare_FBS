s = input('Enter a string: ').lower()
count = 0

for ch in s:
    if ch in 'aeiou':
        count += 1

print('Number of vowels:', count)