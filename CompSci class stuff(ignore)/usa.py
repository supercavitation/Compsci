#Joshua Bloch
#2/21/13
#American flag
#tkinter import code from: http://www.kosbie.net/cmu/fall-10/15-110/handouts/notes-getting-started-with-graphics.html
from Tkinter import *
root = Tk()
canvas = Canvas(root, width=300, height=200)
canvas.pack()
stripes=0
while stripes<=12:
    canvas.create_rectangle(0,1+((200/13)*stripes),300,(200/13)+((200/13)*stripes),fill="red",width=0)
    stripes=stripes+2
canvas.create_rectangle(0,0,150,1400/13-2, fill="dark blue", width=0)
for height in range(0,5):
    oddStars=0
    yTransform=2*(height*(100/9))+3
    while oddStars<=10:
        xTransform=6+((175/13)*(oddStars))
        canvas.create_polygon(0+xTransform,40/9+yTransform,40/13+xTransform,65/9+yTransform,30/13+xTransform,100/9+yTransform,75/13+xTransform,75/9+yTransform,120/13+xTransform,100/9+yTransform,110/13+xTransform,65/9+yTransform,150/13+xTransform,40/9+yTransform,110/13+xTransform,40/9+yTransform,75/13+xTransform,0+yTransform,40/13+xTransform,40/9+yTransform, fill='white')
        oddStars=oddStars+2
for height in range(0,4):
    evenStars=0
    yTransform=2*(height*(100/9))+3+(100/9)
    while evenStars<=8:
        xTransform=6+((175/13)*(evenStars+1))
        canvas.create_polygon(0+xTransform,40/9+yTransform,40/13+xTransform,65/9+yTransform,30/13+xTransform,100/9+yTransform,75/13+xTransform,75/9+yTransform,120/13+xTransform,100/9+yTransform,110/13+xTransform,65/9+yTransform,150/13+xTransform,40/9+yTransform,110/13+xTransform,40/9+yTransform,75/13+xTransform,0+yTransform,40/13+xTransform,40/9+yTransform, fill='white')
        evenStars=evenStars+2
root.mainloop()
