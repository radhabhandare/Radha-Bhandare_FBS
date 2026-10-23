from empmanage import EmpManage
class Main:
    @staticmethod
    def login():
        eid=input("Enter the User Id= ")
        epass=input("Enter the Password= ")
        if eid=="admin" and epass=="1234":
            print("Log in is Done...")
            return True
        else:
            print("Invalid Credentials ")
    def menu(self):
        em=EmpManage()
        while True:
            print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("1.Add Employee ")
            print("2.Display Employee ")
            print("3.Search Employee ")
            print("4.Update Employee ")
            print("5.Delete Employee ")
            print("6.Exit ")
            choice=int(input("Enter Your choice=  "))
            if choice==1:
                em.addEmp()
            elif choice==2:
                em.displyEmp()
            elif choice==3:
                em.searchEmp()
            elif choice==4:
                em.UpdateEmp()
            elif choice==5:
                em.deleteEmp()
            elif choice==6:
                print("Thank you and visit Again Parat ya ")
                break
            else:
                print("Inavalid choice........... ")
res=Main.login()
if res:
    m=Main()
    m.menu()