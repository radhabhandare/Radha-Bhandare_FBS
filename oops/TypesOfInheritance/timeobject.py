class Time:
  def __init__(self, hours, minutes, seconds):
    self.hours = hours
    self.minutes = minutes
    self.seconds = seconds
  def __str__(self):
    return f'{self.hours}:{self.minutes}:{self.seconds}'
  def __add__(self, other):
    
    tseconds = self.seconds + other.seconds
    additional_minutes = tseconds // 60
    tseconds = tseconds % 60
    tminutes = self.minutes + other.minutes + additional_minutes
    additional_hours = tminutes // 60
    tminutes = tminutes % 60
    thours = self.hours + other.hours + additional_hours
    return Time(thours, tminutes, tseconds)
    
t1 = Time(2, 45, 30)
t2 = Time(1, 20, 50)
print(t1+t2)
  