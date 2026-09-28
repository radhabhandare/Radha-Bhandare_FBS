# find max value using indexing
li = [30,24, 90, 82, 99, 55, 22, 33]
max = li[0]
for ind in range(1, len(li)):
  if(li[ind] > max):
    max = li[ind]
    
    
print('maximum:', max)