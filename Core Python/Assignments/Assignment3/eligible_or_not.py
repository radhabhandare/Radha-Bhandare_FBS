#10. Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

gender = input('Enter gender: ')
age = int(input('Enter age: '))

if gender == 'male' and age >= 21:
    print('Eligible to marry')
elif gender == 'female' and age >= 18:
    print('Eligible to marry')
else:
    print('Not eligible to marry')