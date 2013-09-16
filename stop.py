#Joshua Bloch
#2/07/13
#stop sign
from Tkinter import *
root = Tk()
canvas = Canvas(root, width=200, height=200)
canvas.pack()
canvas.create_polygon(58.579,0, 0,58.579,0,141.421,58.579,200,141.421,200,200,141.421,200,58.579,141.421,0, fill="red")
root.mainloop()
