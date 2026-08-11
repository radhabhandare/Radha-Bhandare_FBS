gender = input('enter gender(F/M):')
age = int(input('enter age:'))

if(gender == 'F'):
  if(age>= 18):
    print(' girl is eligble for marriage')
  else:
    print('not elgible')
    
else:
  if(age>=21):
    print('boy is elgible for marriage.')
  else:
    print('boy is not elgible for marriage')