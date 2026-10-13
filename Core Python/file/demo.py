f = None
try:
  f = open("abc.txt","r")
  data = f.read()
  
except Exception as e:
  print(e)
  
else:
  print(data)

finally:
  if f:
    
    f.close()
print('kjdsjk')