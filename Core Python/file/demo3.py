# f = open('demo.txt','w')
# f.write('MI won 5 cups')
# f.writelines(['\n I am good in Mathematics'])

# f =open("demo.txt","a")
# with open("demo.txt","a") as f:
#     f.write("\nI am good in Python")

with open("demo.txt","r+") as f:
  f.seek(3)
  f.writelines(['\nI am good in Python','\nI am good in Java'])
  f.write("I am good in C++")
  print(f.tell())
  data = f.read()
  print(data)