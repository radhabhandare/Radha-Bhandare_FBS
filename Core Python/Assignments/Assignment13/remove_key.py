student = {'name': 'Radha', 'age': 22, 'city': 'Pune'}

key = input('Enter key to remove: ')

if key in student:
    del student[key]
    print('Updated dictionary:', student)
else:
    print('Key does not exist')