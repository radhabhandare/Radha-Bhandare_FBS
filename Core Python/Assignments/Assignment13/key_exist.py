student = {'name': 'Radha', 'age': 22, 'city': 'Pune'}

key = input('Enter key to search: ')

if key in student:
    print('Key exists')
else:
    print('Key does not exist')
