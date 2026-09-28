class Mec():
  def display(self):
    print('display of Mec')
    
class Elec():
  def display(self):
    print('display of Elec')
class Mechatronics(Mec,Elec):
  def abc():
    print('display of Mechatronics')
mech = Mechatronics()
mech.display()