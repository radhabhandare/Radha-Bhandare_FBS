s1 = input('Enter first string: ').lower()
s2 = input('Enter second string: ').lower()

if sorted(s1) == sorted(s2):
    print('Anagrams')
else:
    print('Not anagrams')