
try:
  a = int(input('enter a number1:'))
  b = int(input('enter a number2:'))
  print(a//b)
except ZeroDivisionError as a:
  print(f' I am in zero', a)
except ValueError as v:
  print(f'value err ={v}')
except Exception as e:
  print(e)
else:
  print('i am in else block')
finally:
  print('I am in finally')
# age = int(input('Enter the person age:'))
# print('age')