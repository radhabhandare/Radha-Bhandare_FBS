class Shirt:
  
  small = 0
  medium = 10
  large = 20
  xlarge = 30

  def __init__(self, sid=0, sname='', type='', price=0, size=''):
    self.sid = sid
    self.sname = sname
    self.type = type
    self.price = price
    self.size = size

  def __del__(self):
    print('Shirt object destroyed')

  def ShowBook(self):
    print('Shirt ID:', self.sid)
    print('Shirt Name:', self.sname)
    print('Shirt Type:', self.type)
    print('Size:', self.size)

    if self.size.lower() == 'small':
      final_price = self.price + (self.price * Shirt.small / 100)
    elif self.size.lower() == 'medium':
      final_price = self.price + (self.price * Shirt.medium / 100)
    elif self.size.lower() == 'large':
      final_price = self.price + (self.price * Shirt.large / 100)
    elif self.size.lower() == 'xlarge':
      final_price = self.price + (self.price * Shirt.xlarge / 100)
      
      
    else:
      print('Invalid size')
      return

    print('Original Price:', self.price)
    print('Final Price:', final_price)


s1 = Shirt()
s1.sid = 101
s1.sname = 'Cotton Shirt'
s1.type = 'Formal'
s1.price = 1000
s1.size = 'Small'
s1.ShowBook()

print()

s2 = Shirt(102, 'Casual Shirt', 'Casual', 1000, 'Medium')
s2.ShowBook()

print()

s3 = Shirt(103, 'Office Shirt', 'Formal', 1000, 'Large')
s3.ShowBook()

print()

s4 = Shirt(104, 'Premium Shirt', 'Formal', 1000, 'XLarge')
s4.ShowBook()