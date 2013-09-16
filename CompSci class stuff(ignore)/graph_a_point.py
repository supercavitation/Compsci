#Joshua Bloch
#2/07.13
#grapher
from Tkinter import *
root = Tk()
canvas = Canvas(root, width=300, height=200)
canvas.pack()
canvas.create_line(150,0,150,200)
canvas.create_line(0,100,300,100)
canvas.create_line(145,3,155,3)
for i in range(1,21):
    canvas.create_line(145,10*i,155,10*i)
canvas.create_line(3,95,3,105)
for i in range(1,21):
    canvas.create_line(15*i,95,15*i,105)
choice=int(raw_input('''1) Graph a point
2) Graph a line'''))
xValue=float(raw_input('Enter the x coordinate: '))
yValue=float(raw_input('Enter the y coordinate: '))
xCoordinate=(xValue*15)+150
yCoordinate=(yValue*-10)+100
canvas.create_oval(xCoordinate-1,yCoordinate+1,xCoordinate+1,yCoordinate-1, fill="black")
if choice==2:
    secondXValue=float(raw_input('Enter the second x coordinate: '))
    secondYValue=float(raw_input('Enter the second y coordinate: '))
    secondXCoordinate=(secondXValue*15)+150
    secondYCoordinate=(secondYValue*-10)+100
    canvas.create_oval(secondXCoordinate-1,secondYCoordinate+1,secondXCoordinate+1,secondYCoordinate-1, fill="black")
    canvas.create_line(xCoordinate,yCoordinate,secondXCoordinate,secondYCoordinate)
    if xCoordinate==secondXCoordinate:
        print 'The slope is undefined.'
        print 'The equation of the line is x=', xValue
    else:
        slope= (yValue-secondYValue)/(xValue-secondXValue)

        print ('The slope is'), slope

        if slope==1.0: 
            if yValue-(xValue*slope)==0.0:
                print ('The equation of the line is y=x')
            else:
                if yValue-(xValue*slope)>0:
                    print ('The equation of the line is y=x+'), yValue-(xValue*slope)
                else:
                    print ('The equation of the line is y=x'), yValue-(xValue*slope)
        else:
            if slope==-1.0:
                if yValue-(xValue*slope)==0.0:
                    print ('The equation of the line is y=-x')
                else:
                    if yValue-(xValue*slope)>0:
                        print ('The equation of the line is y=-x+'), yValue-(xValue*slope)
                    else:
                        print ('The equation of the line is y=-x'), yValue-(xValue*slope)
            else:
                if yValue-(xValue*slope)==0.0:
                    print ('The equation of the line is y='), slope, ('x')
                else:
                    if yValue-(xValue*slope)>0:
                        print ('The equation of the line is y='), slope, ('x+'), yValue-(xValue*slope)
                    else:
                        print ('The equation of the line is y='), slope, ('x'), yValue-(xValue*slope)
    root.mainloop()
    
else:
    root.mainloop()

