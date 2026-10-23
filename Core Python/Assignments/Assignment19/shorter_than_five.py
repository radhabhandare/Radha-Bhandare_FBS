s = input('Enter a sentence: ')

words = [i for i in s.split() if len(i) < 5]

print(words)