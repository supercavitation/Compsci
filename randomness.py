import random
import time
from Tkinter import *
root = Tk()
canvas = Canvas(root, width=300, height=200)
canvas.pack()
time.sleep(5)
for i in range(1,1001):
    time.sleep(0.1
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
root.mainloop()
