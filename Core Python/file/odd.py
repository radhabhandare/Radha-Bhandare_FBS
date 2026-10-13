a = [1, 3, 2, 21, 18, 12, 9,5]

count = 0

for i in a:
    if i % 2 != 0:
        if count % 2 == 0:
            print(i)
        count += 1