# 8. Write a program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# failed. (Something like captcha)
userid = input('Enter userid: ')
password = input('Enter password: ')

if userid == 'admin':
    if password == '1234':
        captcha = 5678
        print('Captcha:', captcha)

        num = int(input('Enter captcha: '))

        if num == captcha:
            print('Success')
        else:
            print('Failed')
    else:
        print('Incorrect password')
else:
    print('Incorrect userid')