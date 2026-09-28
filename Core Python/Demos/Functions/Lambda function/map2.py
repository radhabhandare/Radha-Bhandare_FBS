def checkEvenOdd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
      
data = [1,2,3,4,5,6,7,8,9,10]

res = list(map(checkEvenOdd, data))

print(res)