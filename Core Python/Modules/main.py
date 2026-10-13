# import demo1
# demo1.add(12,4)
# print(demo1.pname)

#2 from modulename import member
# from demo1 import add
# add(12,4)

#3 from modulename import members
# from demo1 import add, pname
# add(12, 5)
# print(pname)

#4 from modulename import all(*)
# from demo1 import*
# add(12,4)
# sub(12,5)
# print(pname)

#5. Alicename()
import demo1 as d 
d.add(12,4)
d.sub(12,3)
print(d.pname)