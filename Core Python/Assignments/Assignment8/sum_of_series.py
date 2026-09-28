#1. a. 1+ 2 + 3 + 4+..... + n

# def sum_of_series(n):
#   total = 0
  
#   for i in range(1, n+1):
#     total = total+ i
#   return total

# n = int(input('enter a number:'))
# print('series', sum_of_series(n))

#2. b. 1!+ 2! + 3! + 4!+..... + n!
# def sum_of_factorial(n):
#   total = 0
#   fact = 1
  
#   for i in range(1, n+1):
#     fact = fact*i
    
#     total = total + fact
    
#   return total 

# n = int(input('enter a number:'))

# print('Factorial', sum_of_factorial(n))  

#3 c. 1^1 + 2^2 + 3^3+ ...... n^n

def sum_power(n):
  total = 0
  
  for i in range(1, n+1):
    total = total+ i **i
    
  return total 

n = int(input('enter a number:'))

print('Power', sum_power(n))
