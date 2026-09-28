# def decoretor(a):
#   print(a)
#   a()
  # print('I am in dectoretor')

# print(type(decoretor))
# x = decoretor
# x()

# def login():
#   print('I am in log in')
  
# decoretor(login)

def decoretor(a):
  # print('I am in decoretor')

  def wrapper(*args):
    print('Time started')
    print('Logger Added')
    a(*args)
    print('Time stopped')
    print('Logger remove')
  return wrapper
@decoretor
def login():
  print('\nLog is Done\n')
  
login()
@decoretor
def add(a,b):
  print(a+b)
add(10,20)
