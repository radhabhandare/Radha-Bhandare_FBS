s = input('Enter a sentence: ')

words = s.split()

result = {i: len(i) for i in words}

print(result)