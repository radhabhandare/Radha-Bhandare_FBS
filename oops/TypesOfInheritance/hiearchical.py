class Emp:
  def __init__(self,newname):
    self.name = newname
  def display(self):
    print('Display')
class HR(Emp):
  def display(self):
    print('display of HR')
class Developer(Emp):
  def display(self):
    print('display of Developer')
# hr1 = HR('Rahul')
# hr1.display()
# s1 = Emp('Rahul')
# s1.display()

class JrHR(HR):
  def display(self):
    print('display of JrHR')
class SrHR(HR):
  def display(self):
    print('display of SrHR')
# Jr1 = JrHR('Rahul')
# Jr1.display()

class Jrdev(Developer):
  def display(self):
    print('display of Jrdev')
jrdev = Jrdev('Rahul')
jrdev.display()

class Srdev(Developer):
  def display(self):
    print('display of Srdev')