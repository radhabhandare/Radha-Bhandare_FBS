class Television:
  def __init__(self):
    self.model = 0
    self.screen = 0
    self.price = 0

  def accept(self):
    try:
      self.model = int(input('Enter model number: '))

      if len(str(abs(self.model))) > 4:
        raise ValueError('Model number must have at most 4 digits')

        self.screen = float(input('Enter screen size in inches: '))

      if self.screen < 12 or self.screen > 70:
        raise ValueError('Screen size must be between 12 and 70 inches')

        self.price = float(input('Enter price: '))

      if self.price < 0 or self.price > 5000:
        raise ValueError('Price must be between 0 and 5000')

    except ValueError as e:
      print('Exception:', e)
      self.model = 0
      self.screen = 0
      self.price = 0

  def display(self):
    print('Model Number:', self.model)
    print('Screen Size:', self.screen)
    print('Price:', self.price)


def main():
    tv = Television()
    tv.accept()
    print('\nTelevision Details:')
    tv.display()


main()
