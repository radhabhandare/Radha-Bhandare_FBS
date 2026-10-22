strings = ['python is easy', 'python is useful', 'coding is easy']
words = set()
frequency = {}

for s in strings:
    for word in s.lower().split():
        words.add(word)

        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

print('Unique words:', words)
print('Word frequencies:', frequency)