from Sy.symarks import SYMARKS
from ty.tymarks import TYMarks


class Student:
  def __init__(self, rollno, name, symarks, tymarks):
    self.rollno = rollno
    self.name = name
    self.symarks = symarks
    self.tymarks = tymarks

  def calculateGrade(self):
    total = (self.symarks.ComputerTotal +
             self.tymarks.Theory +
              self.tymarks.Practical)
    
             

    if total >= 70:
      return 'A'
    elif total >= 60:
      return 'B'
    elif total >= 50:
      return 'C'
    elif total >= 40:
      return 'Pass Class'
    else:
      return 'Fail'

  def display(self):
      total = (self.symarks.ComputerTotal +
              self.tymarks.Theory +
              self.tymarks.Practical)

      print('Student Result')
      print('Roll Number:', self.rollno)
      print('Name:', self.name)
      print('SY Computer Marks:', self.symarks.ComputerTotal)
      print('TY Theory Marks:', self.tymarks.Theory)
      print('TY Practical Marks:', self.tymarks.Practical)
      print('Computer Total:', total)
      print('Grade:', self.calculateGrade())


s1 = SYMARKS(25, 30, 28)
t1 = TYMarks(25, 25)

stu = Student(101, 'Radha', s1, t1)
stu.display()