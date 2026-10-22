numbers = [2, 5, -10, 8, -7]
pairs = set()
products = {}

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        pair = (numbers[i], numbers[j])
        pairs.add(pair)
        products[pair] = numbers[i] * numbers[j]

if products:
    max_pair = max(products, key=products.get)
    print('Pair:', max_pair)
    print('Maximum product:', products[max_pair])
else:
    print('At least two numbers are required')
