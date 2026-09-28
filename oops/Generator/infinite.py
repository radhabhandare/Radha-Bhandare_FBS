def infinte():
  i =1 
  while(True):
    yield i
    
    i +=1
res = infinte()

print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))

