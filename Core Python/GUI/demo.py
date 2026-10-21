import tkinter as tk
r =tk.Tk()
r.titile("GUI application")
r.gemometry("500x400")
l1 = tk.label(r,text = "first", bg = "yellow", fg = "blue", font =("Algerian",18))
l2 = tk.label(r,text = "second", bg = "yellow", fg = "blue", font =("Algerian",18))

l3 = tk.label(r,text = "third", bg = "yellow", fg = "blue", font =("Algerian",18))

l4 = tk.label(r,text = "fourth", bg = "yellow", fg = "blue", font =("Algerian",18))

l1.pack(side = "top")
l2.pack(side = "bottom")
l3.pack(side = "left")
l4.pack(side = "right")

e = tk.Entry(r)
#e. insert(0,"enter you name:-")

e.pack()
l2 = tk.label(r,text = "", bg = "yellow", fg = "blue", font =("Algerian",18) )

l2.pack()
def show():
  r = e.get()
  print(r)
r.mainloop()
