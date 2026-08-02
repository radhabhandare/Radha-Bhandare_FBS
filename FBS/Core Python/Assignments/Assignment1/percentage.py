#.1 Write a program to calculate the percentage of student based on marks of any 5 subjencts.

sub1 = float(input('Enter marks of sub1: '))
sub2 = float(input('Enter marks of sub2: '))
sub3 = float(input('Enter marks of sub3: '))
sub4 = float(input('Enter marks of sub4: '))
sub5 = float(input('Enter marks of sub5: '))  

Total = sub1 + sub2 + sub3 + sub4 + sub5
Percentage = (Total / 500) * 100


print('Percentage: ', Percentage)


