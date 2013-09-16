#Sam Smedinghoff
#5/19/13
#Example of how to use a timer to move objects on a TK window
from Tkinter import *
import random
#function that runs every 500 milliseconds
def timer(canvas):
 moveBall(canvas)
 canvas.after(500,timer,canvas)
#function to delete the ball and move it to a new random location
def moveBall(canvas):
 canvas.delete(canvas.data['ball'])
 #get new x and y coordinates 
 x = canvas.data['ballx']+5
 y = canvas.data['bally']+5
 #create new ball and update the data hash
 ball = canvas.create_oval(x,y,x+50,y+50,fill='blue')
 canvas.data['ball'] = ball
 canvas.data['ballx'] = x
 canvas.data['bally'] = y
#Main part of program that sets up the window
window = Tk()
canvas = Canvas(window,width=500,height=500)
canvas.pack()
ball = canvas.create_oval(0,0,50,50,fill='blue') #the ball
#this is a hash/dictionary to keep track of data on the screen
canvas.data = {}
canvas.data['ball']=ball
canvas.data['ballx']=0
canvas.data['bally']=0
timer(canvas) #function that takes care of constantly updating the screen
window.mainloop()
