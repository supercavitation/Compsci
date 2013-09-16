#Joshua Bloch
#4/12/13
#Sorting algorithm
import random
import time
N=160000
#function to sort a list
def mySort(values):
 #Insert code here to sort the list "values"
    if len(values)<=1:
        return values
    pivot=[values[0],values[1]]
    pivot1=[min(pivot)]
    pivot2=[max(pivot)]
    del values[values.index(pivot1[0])]
    del values[values.index(pivot2[0])]
    less=[]
    middle=[]
    greater=[]
    for x in values:
        if x<=pivot1[0]:
            less.append(x)
        elif x>pivot1[0] and x<pivot2[0]:
            middle.append(x)
        else:
            greater.append(x)

    return mySort(less)+pivot1+mySort(middle)+pivot2+mySort(greater)
#You do not need to edit anything below this line
list = []
for i in range(0,N):
 list.append(random.randint(1,N-1))
copy = list[:]
#time the sorting routine
t1 = time.clock()
copy=mySort(copy)
t2 = time.clock()
#make sure the list was sorted correctly
list.sort()
assert(list==copy) 
#print how long the function took to do the sort
print 'mySort took', t2-t1, 'seconds.'
