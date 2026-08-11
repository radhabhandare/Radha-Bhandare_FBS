for i in range(1,6):
  for j in range(1, i +1):
    if(i == 1 or i+j == 6 or i == j):
      print('*', end = ' ')
    else:
      print(' ', end = ' ')
  print()