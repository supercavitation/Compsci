#Based on code from http://www.tkdocs.com/tutorial/firstexample.html#design
#Modified by Sam Smedinghoff and Joshua Bloch
#3/27/13
#GUI calculator
import math
from Tkinter import *

#function to perform the calculation
def equals(*args):
    num1=number.get()
    num1=eval(num1)
    if float(num1)==int(num1):
        num1=int(num1)
    number.set(num1)

#function to add an addition sign    
def add(*args):
    num1=number.get()
    result=str(num1)+'+'
    number.set(result)

#function to add a mulitplication sign    
def multiply(*args):
    num1=number.get()
    result=str(num1)+'*'
    number.set(result)

#function to add a division sign    
def divide(*args):
    num1=number.get()
    result=str(num1)+'/'
    number.set(result)

#function to add a subtraction sign    
def subtract(*args):
    num1=number.get()
    result=str(num1)+'-'
    number.set(result)

#function to add an exponentiation sign
def exponent(*args):
    num1=number.get()
    result=str(num1)+'**'
    number.set(result)

#function to add a modulus sign
def modulus(*args):
    num1=number.get()
    result=str(num1)+'%'
    number.set(result)

#function to add an open parenthesis
def openParenthesis(*args):
    num1=number.get()
    result=str(num1)+'('
    number.set(result)

#function to add a close parenthesis
def closeParenthesis(*args):
    num1=number.get()
    result=str(num1)+')'
    number.set(result)

#function to add a zero
def zero(*args):
    num1=number.get()
    result=str(num1)+'0'
    number.set(result)

#function to add a one
def one(*args):
    num1=number.get()
    result=str(num1)+'1'
    number.set(result)

#function to add a two
def two(*args):
    num1=number.get()
    result=str(num1)+'2'
    number.set(result)

#function to add a three
def three(*args):
    num1=number.get()
    result=str(num1)+'3'
    number.set(result)

#function to add a four
def four(*args):
    num1=number.get()
    result=str(num1)+'4'
    number.set(result)

#function to add a five
def five(*args):
    num1=number.get()
    result=str(num1)+'5'
    number.set(result)

#function to add a six
def six(*args):
    num1=number.get()
    result=str(num1)+'6'
    number.set(result)

#function to add a seven
def seven(*args):
    num1=number.get()
    result=str(num1)+'7'
    number.set(result)

#function to add an eight
def eight(*args):
    num1=number.get()
    result=str(num1)+'8'
    number.set(result)

#function to add a nine
def nine(*args):
    num1=number.get()
    result=str(num1)+'9'
    number.set(result)

#function to add a decimal point
def decimalPoint(*args):
    num1=number.get()
    result=str(num1)+'.'
    number.set(result)

#function to make the number positive or negative        
def negative(*args):
    num1=number.get()
    num1=eval(num1)
    result=int(num1)*(-1)
    number.set(result)    
    
#create window 
window = Tk()
window.title("Calculator")

#create frame to hold the objects in the window
mainframe = Frame(window)
mainframe.grid()

#allows these variables to be used/changed on the window
number = StringVar()

#makes an entry box for the first number and puts it on the grid
number_entry = Entry(mainframe, width=7, textvariable=number)
number_entry.grid(column=1, row=1, sticky=(W, E))

#put an open parenthesis button on frame and link it to the open parenthesis function
Button(mainframe, text="(", command=openParenthesis).grid(column=2, row=2, sticky=W)

#put a close parenthesis button on frame and link it to the close parenthesis function
Button(mainframe, text=")", command=closeParenthesis).grid(column=3, row=2, sticky=W)

#put a modulus button on frame and link it to the modulus function
Button(mainframe, text="mod", command=modulus).grid(column=1, row=2, sticky=W)

#put an exponentiation button on frame and link it to the exponentiation function
Button(mainframe, text='^', command=exponent).grid(column=4, row=2, sticky=W)

#put an addition button on frame and link it to the addition function
Button(mainframe, text="+", command=add).grid(column=4, row=6, sticky=W)

#put a multiplication button on frame and link it to the multiplication function
Button(mainframe, text="x", command=multiply).grid(column=4, row=5, sticky=W)

#put a division button on frame and link it to the division function
Button(mainframe, text="/", command=divide).grid(column=4, row=4, sticky=W)

#put a subtraction button on frame and link it to the subtraction function
Button(mainframe, text="-", command=subtract).grid(column=4, row=3, sticky=W)

#put a - button on frame and link it to the - function
Button(mainframe, text="(-)", command=negative).grid(column=3, row=6, sticky=W)

#put a . button on frame and link it to the . function
Button(mainframe, text=".", command=decimalPoint).grid(column=2, row=6, sticky=W)

#put a 0 button on frame and link it to the 0 function
Button(mainframe, text="0", command=zero).grid(column=1, row=6, sticky=W)

#put a 1 button on frame and link it to the 1 function
Button(mainframe, text="1", command=one).grid(column=1, row=5, sticky=W)

#put a 2 button on frame and link it to the 2 function
Button(mainframe, text="2", command=two).grid(column=2, row=5, sticky=W)

#put a 3 button on frame and link it to the 3 function
Button(mainframe, text="3", command=three).grid(column=3, row=5, sticky=W)

#put a 4 button on frame and link it to the 4 function
Button(mainframe, text="4", command=four).grid(column=1, row=4, sticky=W)

#put a 5 button on frame and link it to the 5 function
Button(mainframe, text="5", command=five).grid(column=2, row=4, sticky=W)

#put a 6 button on frame and link it to the 6 function
Button(mainframe, text="6", command=six).grid(column=3, row=4, sticky=W)

#put a 7 button on frame and link it to the 7 function
Button(mainframe, text="7", command=seven).grid(column=1, row=3, sticky=W)

#put an 8 button on frame and link it to the 8 function
Button(mainframe, text="8", command=eight).grid(column=2, row=3, sticky=W)

#put a 9 button on frame and link it to the 9 function
Button(mainframe, text="9", command=nine).grid(column=3, row=3, sticky=W)

#put an equals button on frame and link it to the calculate function
Button(mainframe, text="=", command=equals).grid(column=4, row=1, sticky=W)

#put words in the correct places on the grid
number_entry.focus() #put cursor in number_entry box
window.mainloop()
