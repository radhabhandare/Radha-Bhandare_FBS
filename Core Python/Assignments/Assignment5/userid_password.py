# 1. Write a program to prompt user to enter userid and password. If Id and password is incorrect give him chance
# to re-enter the credentials. Let him try 3 times. After that program to terminate.

correct_id = 'admin'
correct_password = '1234'

for i in range(3):
    userid = input('Enter User ID : ')
    password = input('Enter Password : ')

    if userid == correct_id and password == correct_password:
        print('Login Successful')
        break
    else:
        print('Invalid User ID or Password')

if userid != correct_id or password != correct_password:
    print('3 attempts completed')