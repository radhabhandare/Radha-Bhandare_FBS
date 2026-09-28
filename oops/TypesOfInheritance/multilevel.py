class Emp:
  def __init__(self,newname):
    self.name = newname
  def display(self):
    print('Display')
class HR(Emp):
  def display(self):
    print('display of HR')
# hr1 = HR('Rahul')
# hr1.display()
# s1 = Emp('Rahul')
# s1.display()

class JrHR(HR):
  def display(self):
    print('display of JrHR')
Jr1 = JrHR('Rahul')
Jr1.display()