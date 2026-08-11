# 7. Write a program to check if user has entered correct userid and password.
userid = input('Enter userid: ')
password = input('Enter password: ')

if userid == 'admin':
    if password == '1234':
        print('Correct userid and password')
    else:
        print('Incorrect password')
else:
    print('Incorrect userid')