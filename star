from Tkinter import *
root = Tk()
canvas = Canvas(root, width=300, height=200)
canvas.pack()
canvas.create_polygon(0+1,40/9+1,40/13+1,60/9+1,30/13+1,100/9+1,75/13+1,50/9+1,120/13+1,100/9+1,110/13+1,60/9+1,150/13+1,40/9+1,110/13+1,40/9+1,75/13+1,0+1,40/13+1,40/9+1, fill='red')
root.mainloop()
