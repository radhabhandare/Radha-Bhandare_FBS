class Product:
  
  def __init__(self, pid=None, pname=None, price=None, quantity=None):
    
    self.pid = pid
    self.pname = pname
    self.price = price
    self.quantity = quantity

  def __del__(self):
    print('Product object destroyed')

  def ShowBook(self):
    print('Product ID:', self.pid)
    print('Product Name:', self.pname)
    print('Price:', self.price)
    print('Quantity:', self.quantity)

p1 = Product()
p1.pid = 1
p1.pname = 'Laptop'
p1.price = 50000
p1.quantity = 2
p1.ShowBook()

print()

p2 = Product(2, 'Mouse', 500, 10)
p2.ShowBook()
