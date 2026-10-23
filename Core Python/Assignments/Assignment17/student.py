class student:
  def __init__(self,StudentId, Name, Age, percentage):
    self.StudentId = StudentId
    self.Name = Name
    self.Age = Age
    self.percentage =percentage
    
    
  def Accept(self):
    self.StudentId = int(input('enter stu Id:'))
    self.Name = input('enter name of stu:')
    self.Age = int(input('enter stu Age:'))
    self.percentage = float(input('enter percentage:'))
    
  def display(self):
    print('Student ID:', self.StudentId)
    print('Name:', self.Name)
    print('Age:', self.Age)
    print('Percentage:', self.percentage)
    
  def calRank(self):
    if self.percentage >= 75:
      return 'Distinction'
    elif self.percentage >= 60:
      return 'first class'
    elif self.percentage >= 50:
      return 'second class'
    elif self.percentage >= 35:
      return 'pass'
    
    else:
      return 'fail'
    
  def __str__(self):
    return f' student Id:{self.StudentId}, Name:{self.Name}, Age:{self.Age}, Percentage:{self.percentage}'

class Engstudent(student):
  def __init__(self, StudentId, Name, Age, percentage, Branch, IA):
    super().__init__(StudentId, Name, Age, percentage)
    self.Branch = Branch
    self.IA = IA
    
  def Accept(self):
    super().Accept()
    self.Branch = input('enter Branch:')
    self.IA = float(input('enter your internal marks:'))
    
  def display(self):
    super().display()
    print('Branch',self.Branch)
    print('Internal marks', self.IA)
    print('Rank', self.calRank())
    
  def calRank(self):
    if self.percentage >= 75:
      return 'Distinction'
    elif self.percentage >= 60:
      return 'first class'
    elif self.percentage >= 50:
      return 'second class'
    elif self.percentage >= 35:
      return 'pass'
        
    else:
      return 'fail'
    
  def __str__(self):
    return f'{super().__str__()} ,Branch:{self.Branch}, Internal Marks:{self.IA}'
  
class Medicalstu(student):
  def __init__(self, StudentId, Name, Age, percentage,specialization, MarksOfInternship):
    super().__init__(StudentId, Name, Age, percentage)
    self.specialization = specialization
    self.MarksOfInternship = MarksOfInternship
    
  def Accept(self):
    super().Accept()
    self.specialization = input('enter your specialization:')
    self.MarksOfInternship = float(input('enter your marks:'))
    
  def display(self):
    super().display()
    print('specialization:',self.specialization)
    print('marksofinternship:', self.MarksOfInternship)
    print('rank:', self.calRank())
  
  def calRank(self):
    if self.percentage >= 75:
      return 'Distinction'
    elif self.percentage >= 60:
      return 'first class'
    elif self.percentage >= 50:
      return 'second class'
    elif self.percentage >= 35:
      return 'pass'
          
    else:
      return 'fail'
    
    
  def __str__(self):
    return f'{super().__str__()}, specialization:{self.specialization}, Internship mraks:{self.MarksOfInternship}'
  
  
class college:
  def __init__(self, number):
    self.number = number
    self.students =[]
    
  def addstu(self,student):
    if len(self.students) < self.number:
      self.students.append(student)
      print('student added successfully')
    else:
      print('not added')
      
  def getstudent(self, studentId):
    for student in self.students:
      if student.StudentId == studentId:
        return student
      
    return None
  
  
  def Removestu(self, studentId):
    for student in self.students:
      if student.StudentId == studentId:
        self.students.remove(student)
        print('student removed')
        return 
    print('student not found')
    
  def __str__(self):
    res = 'college std details:\n'
    for student in self.students:
      res  = res+str(student) + '\n'
    return res
  
s1 = student(100,'Swaroop',23, 75)
s2 = Engstudent(101,'Sanjana',21,80, 'cs',20)
s3 = Medicalstu(103, 'sindhu',22,72,'cardiology', 19)


s1.display()
print('Rank:', s1.calRank())

print()
s2.display()
print('Rank:', s2.calRank())

print()

s3.display()
print()

c1 = college(5)
c1.addstu(s1)
c1.addstu(s2)
c1.addstu(s3)

print(c1)

student = c1.getstudent(100)

if student is not None:
  print('student found:')
  print(student)
  
print()

c1.Removestu(101)

print(c1)