def sum_odd(n):
  total = 0
  for i in range(1, n+1):
    if i %2 != 0:
      total = total + i
      
  return total

n = int(input('enter a number:'))
print('Sum of odd numbers', sum_odd(n))