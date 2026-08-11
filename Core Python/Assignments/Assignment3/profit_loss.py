# 6. Write a program to calculate profit or loss.
cp = float(input('Enter cost price: '))
sp = float(input('Enter selling price: '))

if sp > cp:
    profit = sp - cp
    print('Profit =', profit)
elif cp > sp:
    loss = cp - sp
    print('Loss =', loss)
else:
    print('No profit no loss')