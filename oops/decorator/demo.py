# def demo():
#   print('I am in demo')
  
# # print(type(demo))
# # a = 10
# # print(type(a))
# x = demo
# # demo()
# x()

# def fun(a):
#   a()
# def demo():
#   print('I am in demo')
# x = demo 
# fun(x)

# def outer():
#   print('I am in outer function')
#   def innerFun():
#     print('I am in inner function')
#   return innerFun

# x =outer()
# x()

def outer():
  a = 'virat'
  def inneerFun():
    print(a)
  return inneerFun
x= outer()
x()