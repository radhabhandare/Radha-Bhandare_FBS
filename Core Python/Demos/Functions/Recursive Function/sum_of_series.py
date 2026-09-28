def sos(n):
  if(n <= 0):
    return 0 
  else:
    return n+sos(n-1)
  
num = int(input('Enter a number: '))

res = sos(num)

print(res)
