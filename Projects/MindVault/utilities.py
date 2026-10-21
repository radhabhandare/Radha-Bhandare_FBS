import re
from functools import wraps

def valid_name(name):
  pattern =r"^[A-Za-z ]{2,30}$"
  
  return re.fullmatch(pattern,name)is not None


def show_section(function):
  @wraps(function)
  def wrapper(*args, **kwargs):
    print("\n" + "=" *40)
    result = function(*args,**kwargs)
    print("=" *40)
    return result
  
  return wrapper

def get_choice(mesaage,min,max):
  while True:
    try:
      choice = int(input("enter massage:"))
      if min<= choice <= max:
        return choice
      
      print("enter a number between", min,"And", max)
    
    except ValueError:
      print("Invalid input")
  