numbers = [12, 5, 8, 20, 15]
n = len(numbers)

for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print('Sorted list:', numbers)

largest = numbers[-1]
i = n - 2

while i >= 0 and numbers[i] == largest:
    i -= 1

if i >= 0:
    print('Second largest:', numbers[i])
else:
    print('No second largest distinct number')
