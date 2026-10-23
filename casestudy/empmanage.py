# from hr import Hr
# from dev import Dev
# class EmpManage:
#   Empdetail = {}
#   def addEmp(self):
#     eid = input('Enter Emp Id')
#     if eid in EmpManage.Empdetail:
#       print('Employee is Alredy Exist..')
#       return
#     else:
#       ename = input('Enter th Emp Name =')
#       esal = float(input('Enter Emp sal='))
#       print('1.Hr')
#       print('2.Dev')
#       ch = int(input('Enter your choice='))
#       if ch ==1:
#         ecom=float(input('enter the com of Hr='))
#         emp = Hr(eid,ename,esal,ecom)
#       elif ch ==2:
#         ebonus = float(input('Enter the Bonus of Dev='))
#         emp = Dev(eid,ename,esal,ebonus)
#       else:
#         print('Invalid choice')
#         return
#       EmpManage.Empdetail[eid]=emp
#       print('Employee Added Successfully')
        
#   def DisplyEmp(self):
#     if len(EmpManage.Empdetail)==0:
#       print('Employee is not Exist....')
#     else:
#       for var in EmpManage.Empdetail.values():
#         print(var)
#   def SearchEmp(self):
#     eid = input('Enter Emp Id to Search = ')
#     if eid in EmpManage.Empdetail:
#       emp = EmpManage.Empdetail[eid]
#       print(emp)
#     else:
#       print('Employee is not Exist..')
      
    
      
#   def UpdateEmp(self):
#       eid = input('enter Employee id to update=')
#       if eid in EmpManage.Empdetail:
#         emp = EmpManage.Empdetail[eid]
#         print('1. update name')
#         print('2. update sal')
#         ch = int(input('Enter your choice = '))
#         if ch == 1:
#           newname = input('Enter New Name = ')
#           emp.setName(newname)
#           print('Name Updated Successfully')
#         elif ch == 2:
#           newsal = float(input('Enter New Salary = '))
#           emp.setSal(newsal)
#           print('Salary Updated Successfully')
#         else:
#           print('Invalid choice')
#       else:
#         print('Employee is not Exist....') 
        
#   def DeleteEmp(self):
#       eid = input('Enter Emp Id to Delete = ')
#       if eid in EmpManage.Empdetail:
#         del EmpManage.Empdetail[eid]
#         print('Employee Deleted Successfully')
#       else:
#         print('Employee is not Exist....')
      
      
import mysql.connector  as ct
from hr import Hr
from dev import Dev
class EmpManage:
    @staticmethod
    def getConection():
        con=ct.connect(
            host='localhost',
            user='root',
            password="radha",
            database="employee_db"
        )
        return con
    def addEmp(self):
       eid=input("Enter  Emp Id ")
       con=EmpManage.getConection()
       cur=con.cursor()
       cur.execute("select eid from employees where eid=%s",(eid,))
       if cur.fetchone():
           print("Employee is alredy exist... ")
           cur.close()
           con.close()
       else:
            ename=input("Enter the name of Employee ")
            esal=float(input("Enter the Sal of Employee "))
            print("1.Hr ")
            print("2.Devloper  ")
            ch=int(input("Enter your choice    "))
            if ch==1:
                extra=float(input("Enter the Com of Hr "))
                emp_type="HR"
            elif ch==2:
                extra=float(input("Enter the Bonus of  Devloper  "))
                emp_type="Dev"
            else:
                print("Inavalic choice...  ")
                cur.close()
                con.close()
            qur="insert into employees (eid,ename,esal,emp_type,extra_amount) values(%s,%s,%s,%s,%s)" 
            cur.execute(qur,(eid,ename,esal,emp_type,extra))
            con.commit()
            print("Employee added suseesfully..... ")
            cur.close()
            con.close()
    def displyEmp(self):
        con=EmpManage.getConection()
        cur=con.cursor()
        cur.execute("select * from employees ")
        row=cur.fetchall()
        if not row:
           print("No one is here...")
        else:
            for r in row:
                print(r)
        cur.close()
        con.close()
    def searchEmp(self):
       eid=input("Eneter the id of Eployee to serch employee ")
       con=EmpManage.getConection()
       cur=con.cursor()
       cur.execute('select * from employees where eid=%s',(eid,))
       row=cur.fetchone()
       if row:
           print(row)
       else:
           print("Employee with this  id is not exist..")
           cur.close()
           con.close()
         
    def UpdateEmp(self):
        eid=input("Enter  Emp Id ")
        con=EmpManage.getConection()
        cur=con.cursor()
        cur.execute("select eid from employees where eid=%s",(eid,))
        row=cur.fetchone()
        if not row:
            print("Emp is not  found... ")
            cur.close()
            con.close()
            return
        emp_type=row[0]
        print("1>Update  Devloper")
        print("2>Update  HR")
        ch=int(input("enter the choice"))
        if ch==1 and emp_type=="Dev":
            newname=input("enter the Name of Devloper to update ")
        elif ch==2 and emp_type=="HR":
            newname=input("enter the Name of HR to update ")
        else:
            print("Type ,issamatch or inavlid input")
            cur.close()
            con.close()
            return
        cur.execute("update employees set ename=%s where eis=%s",(newname,eid))
        con.commit()
        print("Employee update ho gaya bhaii ")
        cur.close()
        con.close()
    def deleteEmp(self):
        eid=input("Enter  Emp Id ")
        con=EmpManage.getConection()
        cur=con.cursor()
        cur.execute("select eid from employees where eid=%s",(eid,))
        row=cur.fetchone()
        if not row:
            print("Emp is not  found... ")
            cur.close()
            con.close()
            return
        else:
            cur.execute("delete from employees where eid=%s",(eid,))
            con.commit()
            print("Employee deleted susesfully ")
            cur.close()
            con.close()
            return
      
      
      

