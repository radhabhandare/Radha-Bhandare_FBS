from emp import Employee
class Hr(Employee):
  def __init__(self, id, name,sal,com):
    super().__init__(id,name,sal)
    self.__com = com
  def getCom(self):
    return self.__com
  def setCom(Self,newcom):
    Self.__com = newcom
  def __str__(self):
    return super().__str__()+f'\t Com ={self.__com}'
  