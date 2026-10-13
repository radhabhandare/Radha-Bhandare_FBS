from time import sleep
from threading import Thread

class Demo1(Thread):
  def run(self):
    for i in range(5):
      print("pizza")
      sleep(1)
      
class Demo2(Thread):
  def run(self):
    for i in range(5):
      print("Burger")
      sleep(1)
      
d1 = Demo1()
d2 = Demo2()

d1.start()
d2.start()

d1.join()
d2.join()

print("i am in main")
