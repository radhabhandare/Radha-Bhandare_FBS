from threading import Thread , Lock
from time import sleep
class Bank:
  balance =1000
  l1 = Lock()
  
  def withdraw(self, amount):
    Bank.l1.acquire()
  
    if amount< Bank.balance:
      print("Bank balance =", Bank.balance, "amount =", amount)
      old_balance = Bank.balance
      sleep(1)
      Bank.balance = old_balance - amount
      print("withdrawn amount is:", amount)
    else:
      print("insufficient balance")
      sleep(1)
      Bank.l1.Lock.release()
b1 = Bank()
t1 = Thread(target=b1.withdraw, args=(700,))
t2 = Thread(target=b1.withdraw, args=(500,))
t1.start()
t2.start()
t1.join()
# t2.join()
print("reamaing_balance =", Bank.balance)
