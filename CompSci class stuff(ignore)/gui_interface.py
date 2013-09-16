#Based on code from http://www.tkdocs.com/tutorial/firstexample.html#design
#Modified by Sam Smedinghoff and Joshua Bloch
#3/11/13
#GUI to convert Base 10 numbers to other bases
import math
from Tkinter import *
#function to perform the conversion
def calculate(*args):
    conversion=''
    number1= float(number.get())
    base1=float(base.get())
    digits=int(math.log10(number1)/math.log10(base1))+1
    for place in range (1, digits+1):
        exponent=digits-place
        digit=int(number1/(base1**exponent))
        number1=number1-(base1**exponent)*digit
        if digit<10:
            conversion=conversion+str(digit)
        elif digit==10:
            conversion=conversion+'A'
        elif digit==11:
            conversion=conversion+'B'
        elif digit==12:
            conversion=conversion+'C'
        elif digit==13:
            conversion=conversion+'D'
        elif digit==14:
            conversion=conversion+'E'
        elif digit==15:
            conversion=conversion+'F'
    inBase.set(conversion)
#create window 
window = Tk()
window.title("Bases to Base 10")
#create frame to hold the objects in the window
mainframe = Frame(window)
mainframe.grid()
#allows these variables to be used/changed on the window
number = StringVar()
base =StringVar()
inBase = StringVar()
#makes an entry box for the feet varaible and puts it on the grid
number_entry = Entry(mainframe, width=7, textvariable=number)
number_entry.grid(column=2, row=1, sticky=(W, E))
#makes an empty box for the base variable and puts it on the grid
base_entry = Entry(mainframe, width=7, textvariable=base)
base_entry.grid(column=4, row=2, sticky=(W, E))
#put invisible label for answer on grid
Label(mainframe, textvariable=inBase).grid(column=2, row=2, sticky=(W, E))
#put calculute button on frame and link it to calculate function
Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, 
sticky=W)
#put words in the correct places on the grid
Label(mainframe, text="in base").grid(column=3, row=2, sticky=W)
Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
Label(mainframe, text="in Base 10").grid(column=3, row=1, sticky=W)
number_entry.focus() #put curser in number_entry box
base_entry.focus() #put curser in base_entry box
window.bind('<Return>', calculate) #allow 'Enter' key as well as calculate button
window.mainloop()
