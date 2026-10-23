num = [i for i in range(1, 1001)
       if any(i % j == 0 for j in range(1, 10))]

print(num)