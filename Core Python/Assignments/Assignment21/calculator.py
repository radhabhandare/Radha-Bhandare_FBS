try:
  a = float(input('Enter first number: '))
  b = float(input('Enter second number: '))

  op = input('Enter operator (+, -, *, /): ')

  if op == '+':
    print('Addition:', a + b)

  elif op == '-':
    print('Subtraction:', a - b)

  elif op == '*':
    print('Multiplication:', a * b)

  elif op == '/':
    if b == 0:
      raise ZeroDivisionError('Cannot divide by zero')
    print('Division:', a / b)

  else:
    raise ValueError('Invalid operator')

except ValueError as e:
    print('Error:', e)

except ZeroDivisionError as e:
    print('Error:', e)