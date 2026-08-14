# with passing parameter
# with retuning value

def addition(num1, num2):
  
  add = num1 + num2
  
  return add

num1 = int(input('enter number 1:'))
num2 = int(input('enter number 2:'))


res = addition(num1, num2)

print('Addition:', res)
