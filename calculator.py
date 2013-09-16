#Based on code from http://www.tkdocs.com/tutorial/firstexample.html#design
#Modified by Sam Smedinghoff and Joshua Bloch
#3/11/13
#GUI calculator
import math
from Tkinter import *

#function to perform the conversion
def calculateAdd(*args):
    result=float(firstNumber.get())+float(secondNumber.get())
    if result==int(result):
        result=int(result)
    answer.set(result)
    
def calculateMultiply(*args):
    result=float(firstNumber.get())*float(secondNumber.get())
    if result==int(result):
        result=int(result)
    answer.set(result)
    
def calculateDivide(*args):
    result=float(firstNumber.get())/float(secondNumber.get())
    if result==int(result):
        result=int(result)
    answer.set(result)
    
def calculateSubtract(*args):
    result=float(firstNumber.get())-float(secondNumber.get())
    if result==int(result):
        result=int(result)
    answer.set(result)

def calculateExponent(*args):
    result=float(firstNumber.get())**float(secondNumber.get())
    if result==int(result):
        result=int(result)
    answer.set(result)

def calculateSin(*args):
    angle=(math.pi/180)*float(firstNumber.get())
    result=math.sin(float(angle))
    if result==int(result):
        result=int(result)
    answer.set(result)

def calculateCos(*args):
    angle=(math.pi/180)*float(firstNumber.get())
    result=math.cos(float(angle))
    if result==int(result):
        result=int(result)
    answer.set(result)

def calculateTan(*args):
    angle=(math.pi/180)*float(firstNumber.get())
    result=math.tan(float(angle))
    if result==int(result):
        result=int(result)
    answer.set(result)

def calculateModulus(*args):
    result=float(firstNumber.get())%float(secondNumber.get())
    if result==int(result):
        result=int(result)
    answer.set(result)

def calculateLog(*args):
    result=math.log10(float(firstNumber.get()))
    if result==int(result):
        result=int(result)
    answer.set(result)

def calculateLn(*args):
    result=math.log(float(firstNumber.get()))
    if result==int(result):
        result=int(result)
    answer.set(result)

def calculateLogb(*args):
    result=math.log(float(firstNumber.get()))/math.log(float(secondNumber.get()))
    if result==int(result):
        result=int(result)
    answer.set(result)

def zero(*args):
    if str(window.focus_get())==".4332882256.4332882472":
        num1=firstNumber.get()
        result=str(num1)+'0'
        firstNumber.set(result)
    else:
        num1=secondNumber.get()
        result=str(num1)+'0'
        secondNumber.set(result)
        
def one(*args):
    if str(window.focus_get())==".4332882256.4332882472":
        num1=firstNumber.get()
        result=str(num1)+'1'
        firstNumber.set(result)
    else:
        num1=secondNumber.get()
        result=str(num1)+'1'
        secondNumber.set(result)

def two(*args):
    if str(window.focus_get())==".4332882256.4332882472":
        num1=firstNumber.get()
        result=str(num1)+'2'
        firstNumber.set(result)
    else:
        num1=secondNumber.get()
        result=str(num1)+'2'
        secondNumber.set(result)

def three(*args):
    if str(window.focus_get())==".4332882256.4332882472":
        num1=firstNumber.get()
        result=str(num1)+'3'
        firstNumber.set(result)
    else:
        num1=secondNumber.get()
        result=str(num1)+'3'
        secondNumber.set(result)

def four(*args):
    if str(window.focus_get())==".4332882256.4332882472":
        num1=firstNumber.get()
        result=str(num1)+'4'
        firstNumber.set(result)
    else:
        num1=secondNumber.get()
        result=str(num1)+'4'
        secondNumber.set(result)

def five(*args):
    if str(window.focus_get())==".4332882256.4332882472":
        num1=firstNumber.get()
        result=str(num1)+'5'
        firstNumber.set(result)
    else:
        num1=secondNumber.get()
        result=str(num1)+'5'
        secondNumber.set(result)

def six(*args):
    if str(window.focus_get())==".4332882256.4332882472":
        num1=firstNumber.get()
        result=str(num1)+'6'
        firstNumber.set(result)
    else:
        num1=secondNumber.get()
        result=str(num1)+'6'
        secondNumber.set(result)

def seven(*args):
    if str(window.focus_get())==".4332882256.4332882472":
        num1=firstNumber.get()
        result=str(num1)+'7'
        firstNumber.set(result)
    else:
        num1=secondNumber.get()
        result=str(num1)+'7'
        secondNumber.set(result)

def eight(*args):
    if str(window.focus_get())==".4332882256.4332882472":
        num1=firstNumber.get()
        result=str(num1)+'8'
        firstNumber.set(result)
    else:
        num1=secondNumber.get()
        result=str(num1)+'8'
        secondNumber.set(result)
    
def nine(*args):
    if str(window.focus_get())==".4332882256.4332882472":
        num1=firstNumber.get()
        result=str(num1)+'9'
        firstNumber.set(result)
    else:
        num1=secondNumber.get()
        result=str(num1)+'9'
        secondNumber.set(result)

def decimalPoint(*args):
    if str(window.focus_get())==".4332882256.4332882472":
        num1=firstNumber.get()
        result=str(num1)+'.'
        firstNumber.set(result)
    else:
        num1=secondNumber.get()
        result=str(num1)+'.'
        secondNumber.set(result)
        
def negative(*args):
    if str(window.focus_get())==".4332882256.4332882472":
        num1=firstNumber.get()
        result=int(num1)*(-1)
        firstNumber.set(result)
    else:
        num1=secondNumber.get()
        result=int(num1)*(-1)
        secondNumber.set(result)    
    
#create window 
window = Tk()
window.title("Calculator")

#create frame to hold the objects in the window
mainframe = Frame(window)
mainframe.grid()

#allows these variables to be used/changed on the window
firstNumber = StringVar()
secondNumber =StringVar()
answer = StringVar()

#makes an entry box for the first number and puts it on the grid
firstNumber_entry = Entry(mainframe, width=7, textvariable=firstNumber)
firstNumber_entry.grid(column=1, row=1, sticky=(W, E))

#makes an empty box for the second Number and puts it on the grid
secondNumber_entry = Entry(mainframe, width=7, textvariable=secondNumber)
secondNumber_entry.grid(column=2, row=1, sticky=(W, E))

#put invisible label for answer on grid
Label(mainframe, textvariable=answer).grid(column=3, row=1, sticky=(W, E))

#put a modulus button on frame and link it to calculate function
Button(mainframe, text="mod", command=calculateModulus).grid(column=1, row=2, sticky=W)

#put a log button on frame and link it to calculate function
Button(mainframe, text="log", command=calculateLog).grid(column=2, row=2, sticky=W)

#put an ln button on frame and link it to calculate function
Button(mainframe, text="ln", command=calculateLn).grid(column=3, row=2, sticky=W)

#put a log base b button on frame and link it to calculate function
Button(mainframe, text="logb", command=calculateLogb).grid(column=4, row=2, sticky=W)

#put a sine button on frame and link it to calculate function
Button(mainframe, text="sin", command=calculateSin).grid(column=1, row=3, sticky=W)

#put a cosine button on frame and link it to calculate fuction
Button(mainframe, text="cos", command=calculateCos).grid(column=2, row=3, sticky=W)

#put a tangent button on frame and link it to calculate function
Button(mainframe, text="tan", command=calculateTan).grid(column=3, row=3, sticky=W)

#put an exponentiation button on frame and link it to calculate function
Button(mainframe, text='^', command=calculateExponent).grid(column=4, row=3, sticky=W)

#put an addition button on frame and link it to calculate function
Button(mainframe, text="+", command=calculateAdd).grid(column=4, row=7, sticky=W)

#put a multiplication button on frame and link it to calculate function
Button(mainframe, text="x", command=calculateMultiply).grid(column=4, row=6, sticky=W)

#put a division button on frame and link it to calculate function
Button(mainframe, text="/", command=calculateDivide).grid(column=4, row=5, sticky=W)

#put a subtraction button on frame and link it to calculate function
Button(mainframe, text="-", command=calculateSubtract).grid(column=4, row=4, sticky=W)

#put a - button on frame and link it to the - function
Button(mainframe, text="-", command=negative).grid(column=3, row=7, sticky=W)

#put a . button on frame and link it to the . function
Button(mainframe, text=".", command=decimalPoint).grid(column=2, row=7, sticky=W)

#put a 0 button on frame and link it to the 0 function
Button(mainframe, text="0", command=zero).grid(column=1, row=7, sticky=W)

#put a 1 button on frame and link it to the 1 function
Button(mainframe, text="1", command=one).grid(column=1, row=6, sticky=W)

#put a 2 button on frame and link it to the 2 function
Button(mainframe, text="2", command=two).grid(column=2, row=6, sticky=W)

#put a 3 button on frame and link it to the 3 function
Button(mainframe, text="3", command=three).grid(column=3, row=6, sticky=W)

#put a 4 button on frame and link it to the 4 function
Button(mainframe, text="4", command=four).grid(column=1, row=5, sticky=W)

#put a 5 button on frame and link it to the 5 function
Button(mainframe, text="5", command=five).grid(column=2, row=5, sticky=W)

#put a 6 button on frame and link it to the 6 function
Button(mainframe, text="6", command=six).grid(column=3, row=5, sticky=W)

#put a 7 button on frame and link it to the 7 function
Button(mainframe, text="7", command=seven).grid(column=1, row=4, sticky=W)

#put an 8 button on frame and link it to the 8 function
Button(mainframe, text="8", command=eight).grid(column=2, row=4, sticky=W)

#put a 9 button on frame and link it to the 9 function
Button(mainframe, text="9", command=nine).grid(column=3, row=4, sticky=W)

#put words in the correct places on the grid
firstNumber_entry.focus() #put curser in number_entry box
secondNumber_entry.focus() #put curser in base_entry box
window.mainloop()
