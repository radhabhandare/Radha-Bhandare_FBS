# 2. Enter number of students from user. For those many students accept marks of 5 
# subject marks from user and calculate percentage. Display all percentage and average percentage of students.

n = int(input('Enter number of students : '))

total = 0

for i in range(1, n + 1):
    print('Student', i)

    m1 = float(input('Enter marks of subject 1 : '))
    m2 = float(input('Enter marks of subject 2 : '))
    m3 = float(input('Enter marks of subject 3 : '))
    m4 = float(input('Enter marks of subject 4 : '))
    m5 = float(input('Enter marks of subject 5 : '))

    percentage = (m1 + m2 + m3 + m4 + m5) / 5

    print('Percentage :', percentage)

    total = total + percentage

average = total / n

print('Average Percentage :', average)