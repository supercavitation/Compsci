#Joshua Bloch
#2/22/13
#functions!
import random

#print a string twice
def printTwice(thingToPrint):
    print thingToPrint
    print thingToPrint
    
#print a bunch of qs
def printQs(num):
    print "Q"*num
    
#find the max of two numbers
def bigger(num1,num2):
    if num1>num2:
        print num1
    else:
        print num2
        
#print an even random number        
def randEven(low, high):
    while True:
        randNum=random.randint(low, high)
        if randNum%2==0:
            return randNum
            break
        
#Generate locker combinations
def locker():
    num1=random.randint(0,49)
    num2=random.randint(0,49)
    num3=random.randint(0,49)
    return str(num1)+'-'+str(num2)+'-'+str(num3)
