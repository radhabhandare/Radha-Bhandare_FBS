class A:
  def add(self):
    print('Add a')
class B:
  def add(self):
    print('Add B')
    
class C(B,A):
  def add(self):
    print('Add C')
    
c1 = C()
c1.add()