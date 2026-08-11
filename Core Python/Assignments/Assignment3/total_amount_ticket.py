# 11. Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

age1 = int(input('Enter age of person 1: '))
age2 = int(input('Enter age of person 2: '))
age3 = int(input('Enter age of person 3: '))
age4 = int(input('Enter age of person 4: '))
age5 = int(input('Enter age of person 5: '))

ticket = float(input('Enter ticket amount per person: '))

total = 0

if age1 < 12:
    total = total + ticket * 70 / 100
elif age1 > 59:
    total = total + ticket * 50 / 100
else:
    total = total + ticket

if age2 < 12:
    total = total + ticket * 70 / 100
elif age2 > 59:
    total = total + ticket * 50 / 100
else:
    total = total + ticket

if age3 < 12:
    total = total + ticket * 70 / 100
elif age3 > 59:
    total = total + ticket * 50 / 100
else:
    total = total + ticket

if age4 < 12:
    total = total + ticket * 70 / 100
elif age4 > 59:
    total = total + ticket * 50 / 100
else:
    total = total + ticket

if age5 < 12:
    total = total + ticket * 70 / 100
elif age5 > 59:
    total = total + ticket * 50 / 100
else:
    total = total + ticket

print('Total ticket amount =', total)