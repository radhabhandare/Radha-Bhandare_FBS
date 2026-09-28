from empmanage import EmpManage
class Main:
  @staticmethod
  def login():
    eid =input('Enter the User Id =')
    epass = input('Enter the User Password =')
    
    if eid == 'admin' and epass == '1234':
      print('Login Successfully')
      return True
    else:
      print('Invalid Credential')
  def menu(self):
    em = EmpManage()
    while True:
      
      print('1.Add Employee')
      print('2.Displye Employee')
      print('3.Search Employee')
      print('4.Update Employee')
      print('5. Delete Employee')
      print('6.Exist')
      choice = int(input('Enter your choice ='))
      if choice == 1:
        em.addEmp()
      elif choice ==2:
        em.DisplyEmp()
      elif choice ==3:
        em.SearchEmp()
      elif choice ==4:
        em.UpdateEmp()
      elif choice == 5:
        em.DeleteEmp()
      elif choice == 6:
        print('Thank you visit again')
        break
      else:
       print('Invalid choice')

res = Main.login()
if res:
  m = Main()
  m.menu()
