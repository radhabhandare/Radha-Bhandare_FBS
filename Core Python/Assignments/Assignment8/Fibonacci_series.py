def Fibonacci_series(n):
  a = 0
  b = 1
  if n <= 0:
    print('Please enter a positive integer')
  elif n == 1:
    print(a)
  else:
    print(a, b, end=' ')
    for i in range(2, n):
      c = a + b
      print(c, end=' ')
      a = b
      b = c