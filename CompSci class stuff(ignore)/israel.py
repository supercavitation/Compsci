#Joshua Bloch
#2/07/13
#Israeli flag
from Tkinter import *
root = Tk()
canvas = Canvas(root, width=300, height=200)
canvas.pack()
canvas.create_rectangle(  0,   0, 300, 25, fill="blue")
canvas.create_rectangle(0,  175, 300, 200, fill="blue")
canvas.create_polygon(50,125,150,50,250,125,fill="white", outline="blue", width=3)
canvas.create_polygon(50,75,150,150,250,75,fill="white", outline="blue",width=3)
canvas.create_line(50,125,250,125, fill="blue", width=3)
canvas.create_line(50,125, 150,50,fill="blue", width=3)
canvas.create_line(150,50,250,125,fill="blue",width=3)
root.mainloop()

