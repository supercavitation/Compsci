#Joshua Bloch
#2/07.13
#grapher
from Tkinter import *
root = Tk()
canvas = Canvas(root, width=300, height=200)
canvas.pack()
xValue=float(raw_input('Enter the x coordinate: '))
yValue=float(raw_input('Enter the y coordinate: '))
xCoordinate=(xValue*15)+150
yCoordinate=(yValue*-10)+100
canvas.create_oval(xCoordinate-1,yCoordinate+1,xCoordinate+1,yCoordinate-1, fill="black")
canvas.create_line(150,0,150,200)
canvas.create_line(0,100,300,100)
root.mainloop()
