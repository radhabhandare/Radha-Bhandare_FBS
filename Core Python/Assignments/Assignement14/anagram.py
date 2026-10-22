words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
groups = {}

for word in words:
    key = ''.join(sorted(set(word))) + '|' + ''.join(sorted(word))

    if key in groups:
        groups[key].append(word)
    else:
        groups[key] = [word]

for group in groups.values():
    print(group)