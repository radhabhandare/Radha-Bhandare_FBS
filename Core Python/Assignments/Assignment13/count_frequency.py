s = input('Enter a string: ').lower()
words = s.split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print('Word frequency:', frequency)