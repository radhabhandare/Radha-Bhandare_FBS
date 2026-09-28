class laptop:
    def __init__(self, brand, ram, price):
        self.brand = brand
        self.ram = ram
        self.price = price

    def display(self):
        print(f'brand: {self.brand}\t ram: {self.ram}\t price: {self.price}')


l1 = laptop('Dell', '8GB', 55000)
l2 = laptop('HP', '16GB', 70000)

l1.display()
l2.display()

l2.ram = '32GB'
l2.display()

print(l1.brand)