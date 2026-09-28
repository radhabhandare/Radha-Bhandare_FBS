class student:
  inName ='FBS'
  stdCount = 0
  @staticmethod
  # def Greet():
  #   print('Welcome.....')
  def getInName():
    return student.inName
  @staticmethod
  def setInName(newname):
    student.inName = newname
    
  def __init__(self,RollNo,Name,BatchName):
    self.RollNo = RollNo
    self.Name = Name
    self.BatchName = BatchName
    student.stdCount += 1
  
  def display(self):
    print(f'RollNO: {self.RollNo}\t Name: {self.Name}\t BatchName: {self.BatchName}\t InstituteName={student.inName}')
    
s1 = student(12, 'suraj', 'jp')
s2 = student(13, 'swaraj','jp')
s3 = student(1,'Ritik','jup')

s1.display()
s2.display()
s3.display()


# student.inName= 'firstbitsolutions'

# print('+++++++++++++')
# s1.display()
# s2.display()
# s3.display()
# student.Greet()
# s1.Greet()

print(student.stdCount)