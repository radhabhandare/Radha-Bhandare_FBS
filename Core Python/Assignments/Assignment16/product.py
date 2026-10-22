class Product:
  discount = 10

  def __init__(self, pid=0, pname='', price=0, quantity=0):
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

  def ApplyDiscount(self):
    dprice = self.price - (self.price * Product.discount / 100)
    print('Price After Discount:', dprice)


p1 = Product()
p1.pid = 1
p1.pname = 'Laptop'
p1.price = 50000
p1.quantity = 2
p1.ShowBook()
p1.ApplyDiscount()

print()

p2 = Product(2, 'Headphones', 2000, 5)
p2.ShowBook()
p2.ApplyDiscount()
