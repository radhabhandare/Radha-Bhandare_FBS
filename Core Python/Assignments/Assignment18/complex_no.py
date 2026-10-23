class complex:
  def __init__(self, real , imag):
    self.real = real
    self.imag = imag
    
  def __add__(self, other):
    r = self.real + other.real
    i = self.imag + other.imag
    return complex(r, i)
  
  def __sub__(self, other):
    r = self.real - other.real
    i = self.imag - other.imag
    return complex(r, i)
  
  def display(self):
    print(self.real , '+', self.imag, 'i')
    
  def __del__(self):
    print('complex object del')
c1 = complex(10,3)
c2 = complex(20,4)

c3 = c1+c2
print('addition:')
c3.display()

c4 = c2-c1
print('substraction:')
c4.display()
