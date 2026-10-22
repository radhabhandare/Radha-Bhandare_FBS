s = input('Enter a string: ').lower()
words = s.split()
count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

for word in count:
    print(word, ':', count[word])