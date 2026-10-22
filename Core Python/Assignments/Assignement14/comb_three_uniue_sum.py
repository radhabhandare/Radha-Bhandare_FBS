numbers = [1, 2, 3, 4, 5, -1, 0]
target = int(input('Enter target sum: '))

combinations = set()

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        for k in range(j + 1, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == target:
                combination = tuple(sorted(
                    (numbers[i], numbers[j], numbers[k])
                ))
                combinations.add(combination)

print('Combinations:', combinations)