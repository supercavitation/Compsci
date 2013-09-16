#Joshua Bloch
#3/12/13
#bubbles
import random
from Tkinter import *
root = Tk()
canvas = Canvas(root, width=300, height=200)
canvas.pack()
def bubbles(event):
    num=random.randint(1,4)
    if num==1:
        canvas.configure(bg='red')
    elif num==2:
        canvas.configure(bg='yellow')
    elif num==3:
        canvas.configure(bg='green')
    else:
        canvas.configure(bg='blue')
    xValue=random.randint(1,300)
    yValue=random.randint(1,200)
    radius=random.randint(10,25)
    color=random.randint(1,6)
    if color==1:
        color='red'
    elif color==2:
        color='blue'
    elif color==3:
        color='yellow'
    elif color==4:
        color='green'
    elif color==5:
        color='purple'
    else:
        color='orange'
    canvas.create_oval(xValue+radius,yValue-radius,xValue-radius,yValue+radius, fill=color)
root.bind("<Button-1>",bubbles)
root.mainloop()
