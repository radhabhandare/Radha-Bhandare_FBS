from time import sleep
from threading import Thread

def fun1():
  for i in range(5):
    print("Sindhu")
    sleep(1)
def fun2():
  for i in range(5):
    print("sanjana")
    sleep(1)

t1 = Thread(target=fun1)
t2 = Thread(target=fun2)

t1.start()
t2.start()
t1.join()
t2.join()

print("I am in main Thread")