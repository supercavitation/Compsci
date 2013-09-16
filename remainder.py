#Joshua Bloch
#2/07/13
#remainder game
import random
from Tkinter import *
root = Tk()
divisor=random.randint(1,10)
dividend=random.randint(20,30)
print 'What is the remainder when', dividend, 'is divided by', divisor, '?'
problem=int(raw_input('The remainder is: '))
if problem==dividend%divisor:
    canvas = Canvas(root, width=300, height=300)
    canvas.pack()
    canvas.create_oval(5,5,300,300, fill="white", width=3)
    canvas.create_oval(75,75,100,100, fill="white", width=3)
    canvas.create_oval(225,75,200,100, fill="white", width=3)
    canvas.create_oval(75,105,225,250, fill="white", width=3)
    canvas.create_rectangle(70,104,230,175,fill="white", width=0)
else:
    canvas = Canvas(root, width=300, height=300)
    canvas.pack()
    canvas.create_oval(5,5,300,300, fill="white", width=3)
    canvas.create_oval(75,75,100,100, fill="white", width=3)
    canvas.create_oval(225,75,200,100, fill="white", width=3)
    canvas.create_oval(75,105,225,250, fill="white", width=3)
    canvas.create_rectangle(70,175,230,255,fill="white",width=0)
root.mainloop()
