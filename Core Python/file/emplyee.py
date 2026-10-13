#WAP to create class of employee & add the emp object into a file
import pickle
class Employee:
    def __init__(self, emp_id, name, department):
        self.emp_id = emp_id
        self.name = name
        self.department = department

    def __str__(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}, Department: {self.department}"
with open("employee.txt", "a+") as f:
    e1 = Employee(101, "shiv", "HR")
    e2 = Employee(102, "Ravi", "IT")
    # f.write(str(e1))
    # f.write(str(e2))
    # f.write("\n") 
    # d =f.read()
    # # print(d)
    # d.setid(102)
    # print(d.getname())
f = open("emp.dat", "rb")
#pickle.dump("objectname",object of file)
pickle.dump("e1",f)
