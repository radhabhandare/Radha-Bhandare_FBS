class Emp:
  def calsal(self):
    print('Emp calsal')
class Hr(Emp):
  pass
  # def calsal(self):
  #   print('Hr calsal')
    
class Admin(Emp):
  pass
  # def calsal(self):
  #   print('Add C')
    
h1 = Hr()
h1.calsal()

a = Admin()
a.calsal()