#1. pass : to neglect expected indentation block error
for i in range(1, 10):
   pass
 
 
#2. break : to terminate the loop (stop the loop)
# for i in range(1, 10):
#   if (i ==3):
#     break
#   print(i)
  

#3. continue : to skip the current iteration of the loop and continue with the next iteration

# for i in range(1, 10):
#   if (i ==3):
#     continue
#   print(i)
  

#4. else : will wxeccute when loop executed successfully

for i in range(1, 10):
  if (i ==3):
    break
  print(i)
  
else:
  print('Else executed.')
  