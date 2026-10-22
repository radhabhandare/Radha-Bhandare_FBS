class shirt:
  def __init__(self,sid = None, sname = None, type = None, price = None, size = None):
    self.sid = sid
    self.sname = sname
    self.type = type
    self.price = price
    self.size = size
    
  def __delete__(self):
    
    print('destroyed')
    
  def showBook(self):
    print('shirt Id:', self.sid)
    print('shirt name:', self.sname)
    print('type:', self.type)
    print('shirt price:',self.price)
    print('size:', self.size)
    
s1=shirt()
s1.sid = 101
s1.sname = 'cotton'
s1.type = 'formal'
s1.price = 500
s1.size = 'medium'
s1.showBook()

print()

s2 = shirt(102,'mix', 'casual',700, 'large')
s2.showBook()
  
  