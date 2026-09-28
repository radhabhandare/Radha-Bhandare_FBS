#!. for memory optimization
#2. generating values according to user requirement
#3. use Yield keyword
#4. maintain state(maintain stack frame) of function 

#5. iterate upcoming values using nect from iterables

def generatorvalues(n):
  for i in range(1,n+1):
    yield i
    
res = generatorvalues(5)

print(next(res))
print(next(res))

print(next(res))
print(next(res))
print(next(res))

