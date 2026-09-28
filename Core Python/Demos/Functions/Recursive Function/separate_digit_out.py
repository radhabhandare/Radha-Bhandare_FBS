# Wap to separate out digits using recursive function 

def separate(n):
  if n == 0:
    return 
  else:
    separate (n // 10 )
    print(n % 10)
    
num = int(input('enter a number:'))

res= separate(num)
print(res)