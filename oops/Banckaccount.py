class account:
    def __init__(self, name, balance, accounttype):
        self.name = name
        self.balance = balance
        self.accounttype = accounttype
    def getname(self):
        return self.name
    def setname(self,newname):
        self.id = newname
    def getbalance(self):
      return self.balance
    def setbalance(self, newbalance):
      self.balance = newbalance

    def display(self):
        print(f'name: {self.name}\t balance: {self.balance}\t type: {self.accounttype}')


a1 = account('Rahul', 50000, 'Savings')
a2 = account('Priya', 75000, 'Current')

a1.display()
a2.display()

a1.balance = 60000
a1.display()

print(a2.accounttype)