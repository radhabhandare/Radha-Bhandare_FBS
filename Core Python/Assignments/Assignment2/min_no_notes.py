# Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.

amount = int(input('Enter amount: '))

note500 = amount // 500
amount = amount % 500

note200 = amount // 200
amount = amount % 200

note100 = amount // 100
amount = amount % 100

note50 = amount // 50
amount = amount % 50

note20 = amount // 20
amount = amount % 20

note10 = amount // 10

total_notes = note500 + note200 + note100 + note50 + note20 + note10

print('Minimum number of notes =', total_notes)