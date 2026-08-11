x= 10 
y = 10 
z = 20
li1 = [10 , 20 ] # Mutable - new memory location will be created for new list 
li2 = [10 , 20 ]

print(id(x))
print(id(y))
print(id(z))
print(x is y) # True
print(x is z) # False

print(id(li1))
print(id(li2))

print(li1 is li2) # False
