# Our function is object of function class
#we can stored the fun in variable..
# def demo():
#     print("I am in demo")
# x=demo
# # demo()
# x()
# def demo(a):
#     a()
# def fun():
#     print("I am in tested function")    
# demo(fun)

# return one function from other function
# def outerfun():
#     print("I am in outer ")
#     def innerfun():
#         print("I am in inner function")
#     return innerfun
#     # return 10
# result=outerfun()
# result()

   
# def demo():
#     a="FBS"
#     def innerfun():
#         print("I am in innerfunction",a)
#     return innerfun
# res=demo()
# res()


def decore(a):
    # print("I am in decorer")
    def innerfun(*args):
        print("Time started ")
        print("Logger added")
        a(*args)
        print("Time Stopeed")
        print("Logger removed ")
    return innerfun 
@decore
def login():
    print("Log in is Done")
    
@decore
def logout():
    print("Logout in is Done")

@decore
def add(a,b):
    print(f"Addition ={a+b}")

add(12,23)

# res=decore(login)
# res()

login()
# logout()