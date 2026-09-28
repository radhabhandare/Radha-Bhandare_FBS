def sum_prime(n):
  total = 0
  for i in range(1, n+1):
    for j in range(2, i):
      if i % j == 0:
        break
    else:
      total = total + i
      
  return total

n = int(input('enter a number:'))
print('Sum of prime numbers', sum_prime(n))
