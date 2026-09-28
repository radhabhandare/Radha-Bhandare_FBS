from hr import Hr
from dev import Dev
class EmpManage:
  Empdetail = {}
  def addEmp(self):
    eid = input('Enter Emp Id')
    if eid in EmpManage.Empdetail:
      print('Employee is Alredy Exist..')
      return
    else:
      ename = input('Enter th Emp Name =')
      esal = float(input('Enter Emp sal='))
      print('1.Hr')
      print('2.Dev')
      ch = int(input('Enter your choice='))
      if ch ==1:
        ecom=float(input('enter the com of Hr='))
        emp = Hr(eid,ename,esal,ecom)
      elif ch ==2:
        ebonus = float(input('Enter the Bonus of Dev='))
        emp = Dev(eid,ename,esal,ebonus)
      else:
        print('Invalid choice')
        return
      EmpManage.Empdetail[eid]=emp
      print('Employee Added Successfully')
        
  def DisplyEmp(self):
    if len(EmpManage.Empdetail)==0:
      print('Employee is not Exist....')
    else:
      for var in EmpManage.Empdetail.values():
        print(var)
  def SearchEmp(self):
    eid = input('Enter Emp Id to Search = ')
    if eid in EmpManage.Empdetail:
      emp = EmpManage.Empdetail[eid]
      print(emp)
    else:
      print('Employee is not Exist..')
      
    
      
  def UpdateEmp(self):
      eid = input('enter Employee id to update=')
      if eid in EmpManage.Empdetail:
        emp = EmpManage.Empdetail[eid]
        print('1. update name')
        print('2. update sal')
        ch = int(input('Enter your choice = '))
        if ch == 1:
          newname = input('Enter New Name = ')
          emp.setName(newname)
          print('Name Updated Successfully')
        elif ch == 2:
          newsal = float(input('Enter New Salary = '))
          emp.setSal(newsal)
          print('Salary Updated Successfully')
        else:
          print('Invalid choice')
      else:
        print('Employee is not Exist....') 
        
  def DeleteEmp(self):
      eid = input('Enter Emp Id to Delete = ')
      if eid in EmpManage.Empdetail:
        del EmpManage.Empdetail[eid]
        print('Employee Deleted Successfully')
      else:
        print('Employee is not Exist....')
      
      
