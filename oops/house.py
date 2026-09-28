class house:
    def __init__(self, location, price, rooms):
        self.location = location
        self.price = price
        self.rooms = rooms

    def display(self):
        print(f'location: {self.location}\t price: {self.price}\t rooms: {self.rooms}')


h1 = house('Pune', 5000000, 2)
h2 = house('Mumbai', 8000000, 3)

h1.display()
h2.display()

h2.price = 7500000
h2.display()

print(h1.location)