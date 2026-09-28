class car:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color
        
      
    def display(self):
       print(f'brand: {self.brand}\t price: {self.price}\t color: {self.color}')


c1 = car('Toyota', 1500000, 'White')
c2 = car('Honda', 1200000, 'Black')

c1.display()
c2.display()

c1.color = 'Red'
c1.display()

print(c2.brand)