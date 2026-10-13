#1. direct import
# import mypack.abc
# import mypack.xyz
# mypack.abc.greet()

# mypack.xyz.greet1()

#2 from packagename.modulename import member

# from mypack.abc import greet
# greet()

#3 forom packagename.modulename import members

# from mypack.xyz import greet1, iname

# greet1()

#4 from packagename.modulename import all(*)

# from mypack.xyz import*

# greet1()

#5 Aicename

import mypack.xyz as a

print(a.iname)
