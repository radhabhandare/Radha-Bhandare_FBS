import random
# print(int(random.random()*1000))

# print(random.randint(100,999))  includes both number 
# print(random.randrange(1000,10000)) # exclude last number

# li =["virat", "Msd","Rohit","Sachin"]
# print(random.choice(li))
# print(li)
# random.shuffle(li)

# print(li)

import time
# print(time.time())
# for i in range(1,10):
#   time.sleep(1)
#   print(i)

# print(time.ctime())

# t = time.localtime()
# print(t.tm_year)
# print(t.tm_mday)


import datetime
#date, time, datetime, timedelta

# print(datetime.date.today())

# print(datetime.datetime.now())

now = datetime.datetime.now()
print(now.year)
print(now.month)
print(now.hour)
print(now.min)
print(now.second)