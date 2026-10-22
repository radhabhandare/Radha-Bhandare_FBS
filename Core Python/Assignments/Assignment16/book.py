class Book:
  count = 0

  def __init__(self, bid=0, bname='', price=0, author=''):
    self.bid = bid
    self.bname = bname
    self.price = price
    self.author = author
    Book.count = Book.count + 1

  def __del__(self):
    print('Book object destroyed')

  def ShowBook(self):
    print('Book ID:', self.bid)
    print('Book Name:', self.bname)
    print('Price:', self.price)
    print('Author:', self.author)


b1 = Book()
b1.bid = 101
b1.bname = 'The Art of Being Alone'
b1.price = 299
b1.author = 'Renuka Gavrani'
b1.ShowBook()

print()

b2 = Book(102, 'The Mountain Is You', 350, 'Brianna Wiest')
b2.ShowBook()

print('Total Book Objects:', Book.count)
