class MyException(Exception):
  def __init__(self, *args):
    self.age = args
    print('invalid age')
  def __str__(self):
    return f'bhai enter age'  
    