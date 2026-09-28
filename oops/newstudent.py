class student:
  inName ='FBS'
  stdCount = 0
  def __init__(self,RollNo,Name,BatchName):
      self.RollNo = RollNo
      self.Name = Name
      self.BatchName = BatchName
      student.stdCount += 1
  def setRollno(self,nrollno):
      self.RollNo = nrollno
  def display(self):
      print(f'RollNO: {self.RollNo}\t Name: {self.Name}\t BatchName: {self.BatchName}\t InstituteName={student.inName}')

class placedstudent(student):
  inName ='FBS'
  def __init__(self,RollNo,Name,BatchName,CompanyName):
      super().__init__(RollNo,Name,BatchName)
      self.CompanyName = CompanyName
  def display(self):
      print(f'CompanyName = {self.CompanyName}')
      return super().display()
s1 = student(12, 'suraj', 'jp')
s2 = placedstudent(13, 'swaraj','jp','TCS')
print(student.stdCount)