class distance:
  def __init__(self, km , m ,cm):
    self.km = km 
    self.m = m
    self.cm = cm 
  
  def __add__(self, other):
    d1 = self.km*100000 + self.m *100 +self.cm
    d2 = self.km*100000 + self.m *100 +self.cm
    
    total = d1 + d2
    
    km = total // 100000
    m = total % 100000
    m = m //100
    cm = total % 100
    
    return distance(km, m , cm)
  
  def __sub__(self, other):
    d1 = self.km*100000 + self.m *100 +self.cm
    d2 = self.km*100000 + self.m *100 +self.cm
    
    total = d1 - d2
    
    km = total // 100000
    m = total % 100000
    m = m //100
    cm = total % 100
    
    return distance(km, m , cm)
  
  def display(self):
    print('distance obj del')

d1 = distance(2, 500, 70)
d2 = distance(1, 200, 50)

print('first distance')
d1.display()
print('second distance')
d2.display()

d3 = d1+d2
print('additon:')
d3.display()

d4 = d1- d2
print('sub:')
d4.display()