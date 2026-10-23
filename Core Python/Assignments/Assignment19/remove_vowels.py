s = input('Enter a string: ')

result = ''.join([i for i in s if i.lower() not in 'aeiou'])

print(result)