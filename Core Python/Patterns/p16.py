# for i in range(1,6):
#   for j in range(6 - i):
#     print(' ', end = ' ')
    
#   for j in range(1, i * 2):
#     print(j, end = ' ')
    
    
#   print()


for i in range(1,6):
  k = 1
  for j in range(1, 6 - i):
    print(' ', end = ' ')
    
  for j in range(1, i +1):
    print(k, end = ' ')
    k += 1
    
  for j in range(1, i):
    print(k , end = ' ')
    
    k +=1
  print()