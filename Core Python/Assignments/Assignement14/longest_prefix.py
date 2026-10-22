words = ['flower', 'flow', 'flight']

prefix = ''

for i in range(len(min(words, key=len))):
    chars = set()

    for word in words:
        chars.add(word[i])

    if len(chars) == 1:
        prefix += words[0][i]
    else:
        break

print('Longest common prefix:', prefix)