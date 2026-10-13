import pickle
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
e1 = Employee(101,"sanjana",10000)
e2 = Employee(102,"Radha",20000)
e3 = Employee(103,"Swaroop",30000)
e4 = Employee(104,"Prathmesh",40000)
e5 = Employee(105,"Ashutosh",50000)
  
f = open("Employee.dat","wb")
print(f.tell())
pickle.dump(e1,f)
pickle.dump(e2,f)
pickle.dump(e3,f)
fr = open("Employee.dat","rb")
f.seek(0)

data =pickle.load(fr)
print(data)

data1 =pickle.load(fr)
print(data1)

fa = open("Employee.dat","ab")
f.seek(0,2)
pickle.dump(e4,fa)

fw = open("Employeee.dat","wb+")

fw.tell()
pickle.dump(e1,fw)

# frb = open("Employeee.dat","rb+")

# data4 =pickle.load(frb)
# print(data4)

fab = open("Employeee.dat","ab+")
f.seek(0)
pickle.dump(e5,fab)