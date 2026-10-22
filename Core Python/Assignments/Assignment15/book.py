class Book:
  
  def __init__(self, bid=None, bname=None, price=None, author=None):
    self.bid = bid
    self.bname = bname
    self.price = price
    self.author = author

  def __del__(self):
    print('Book object destroyed')

  def ShowBook(self):
    print('Book ID:', self.bid)
    print('Book Name:', self.bname)
    print('Price:', self.price)
    print('Author:', self.author)


# Parameterless constructor
b1 = Book()
b1.bid = 101
b1.bname = 'The Art of Being Alone'
b1.price = 300
b1.author = 'Renuka Gavrani'
b1.ShowBook()

print()

# Parameterized constructor
b2 = Book(102, 'The Mountain Is You', 350, 'Brianna Wiest')
b2.ShowBook()
