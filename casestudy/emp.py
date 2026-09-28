class Employee:
  def __init__(self,id, name,sal):
    self.__id = id
    self.__name = name
    self.__salary = sal

  def getId(self):
    return self.__id
  def setId(self,newid):
    self.__id = newid
  
  def getName(self):
    return self.__name
  def setName(self,newname):
    self.__name = newname
    
  def getSalary(self):
    return self.__salary
  def setSal(self,newsal):
    self.__salary = newsal
    
  def __str__(self):
    return f'Id={self.__id}\tName = {self.__name}\tSal = {self.__salary}'

    
