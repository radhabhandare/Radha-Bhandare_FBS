num = int(input('enter number:'))

if(num <= 0):
  print('less than or equal tp zero.')
elif(num <= 50):
  print('1 - 50')
elif(num <= 100):
  print('51 - 100')
elif(num <= 150):
  print('101 - 150')
elif(num <= 250):
  print('151 - 250')
else:
  print('greater than 250')