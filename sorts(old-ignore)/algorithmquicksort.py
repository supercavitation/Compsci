#Joshua Bloch
#4/12/13
#Sorting algorithm
import random
import time
from numpy.random import randint

N=170000
#function to sort a list
def smedserSort(values):
 #Insert code here to sort the list "values"
    if len(values)<=1:
        return values
    
    if len(values)<=20:
        for i in range(1,len(values)):
            value=values[i]
            hole=i
            while hole>0 and value<values[hole-1]:
                values[hole]=values[hole-1]
                hole-=1
            values[hole]=value
        return values
    
    if values[0]>values[1]:
        values[0], values[1]=values[1],values[0]
    if values[0]>values[2]:
        values[0],values[2]=values[2],values[0]
    if values[1]>values[2]:
        values[1],values[2]=values[2],values[1]
    
    less=[]
    firstMiddle=[]
    secondMiddle=[]
    greater=[]
    
    for x in values[3:]:
        if x<=values[0]:
            less.append(x)
        elif x>values[0] and x<values[1]:
            firstMiddle.append(x)
        elif x>=values[1] and x<values[2]:
            secondMiddle.append(x)
        else:
            greater.append(x)

    less=smedserSort(less)
    firstMiddle=smedserSort(firstMiddle)
    secondMiddle=smedserSort(secondMiddle)
    greater=smedserSort(greater)

    less.append(values[0])
    firstMiddle.append(values[1])
    secondMiddle.append(values[2])

    return less+firstMiddle+secondMiddle+greater
#You do not need to edit anything below this line
list = []
for i in range(0,N):
 list.append(random.randint(1,N-1))
copy = list[:]
#time the sorting routine
t1 = time.clock()
copy=smedserSort(copy)
t2 = time.clock()
#make sure the list was sorted correctly
list.sort()
assert(list==copy) 
#print how long the function took to do the sort
print 'mySort took', t2-t1, 'seconds.'
