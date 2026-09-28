class Employee:
  def __init__(self,id, name,sal):
    self.id = id
    self.name = name
    self.salary = sal
    
  def getId(self):
    return self.id
  def setId(self,newid):
    self.id = newid
  
  def getName(self):
    return self.name
  def setName(self,newname):
    self.name = newname
    
  def getSalary(self):
    return self.salary
  def setSal(self,newsal):
    self.sal = newsal
    
    
  def display(self):
    print(f'id: {self.id}\t name: {self.name}\t salary: {self.salary}')
  def calsal(self):
    print('Emp sal =', {self.salary})
    

class Hr(Employee):
  def __init__(self,id, name,sal,commission):
    super().__init__(id, name,sal)
    self.commission = commission
    
  def getDept(self):
    return self.dept
  def calsal(self,newcommission):
    self.commission = newcommission
    
    
  def display(self):
    print(f'id: {self.id}\t name: {self.name}\t salary: {self.salary}\t dept: {self.dept}')
  def calsal(self):
    print(f' final salary of hr is {self.commission+self.getSalary()}')

class Developer(Employee):
  def __init__(self,id, name,sal,bonous):
    super().__init__(id, name,sal)
    self.bonous = bonous
    
  def getTech(self):
    return self.tech
  def calsal(self,newbonous):
    self.bonous = newbonous
    
  def display(self):
    print(f'id: {self.id}\t name: {self.name}\t salary: {self.salary}\t tech: {self.tech}')
    
  def calsal(self):
    print(f' final salary of developer is {self.bonous+self.getSalary()}')

e1 = Employee(101,'Ramesh',50000)
h1 = Hr(102,'Suresh',60000,10000)
d1 = Developer(103,'Mahesh',70000,15000)
e1.calsal()
h1.calsal()
d1.calsal()


print(e1)