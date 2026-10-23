s = input('Enter a string: ')

count = sum([1 for i in s if i == ' '])

print('Number of spaces:', count)