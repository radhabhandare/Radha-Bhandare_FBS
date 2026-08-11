#8. Write a program to convert days into years, weeks and days.

days = int(input('Enter number of days: '))

years = days // 365
remaining = days % 365

weeks = remaining // 7

days_left = remaining % 7

print('Years: ', years)
print('Weeks: ', weeks)
print('Days: ', days_left)
  
