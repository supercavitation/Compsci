#Joshua Bloch
#4/12/13
#Sorting algorithm
import random
import time
N=1000000
#function to sort a list
def mySort(values):
 #Insert code here to sort the list "values"
    if len(values)<=1:
        return values
    if len(values)<=15:
        for i in range(1,len(values)):
            value=values[i]
            hole=i
            while hole>0 and value<values[hole-1]:
                values[hole]=values[hole-1]
                hole-=1
            values[hole]=value
        return values
    pivot=[values[0],values[1],values[2],values[3],values[4]]
    pivot1=[min(pivot)]
    pivot.remove(min(pivot))
    pivot2=[min(pivot)]
    pivot.remove(min(pivot))
    pivot3=[min(pivot)]
    pivot.remove(min(pivot))
    pivot4=[min(pivot)]
    pivot5=[max(pivot)]
    del values[values.index(pivot1[0])]
    del values[values.index(pivot2[0])]
    del values[values.index(pivot3[0])]
    del values[values.index(pivot4[0])]
    del values[values.index(pivot5[0])]
    less=[]
    firstMiddle=[]
    middle=[]
    secondMiddle=[]
    thirdMiddle=[]
    greater=[]
    for x in values:
        if x<=pivot1[0]:
            less.append(x)
        elif x>pivot1[0] and x<=pivot2[0]:
            firstMiddle.append(x)
        elif x>pivot2[0] and x<=pivot3[0]:
            middle.append(x)
        elif x>pivot3[0] and x<=pivot4[0]:
            secondMiddle.append(x)
        elif x>pivot4[0] and x<=pivot5[0]:
            thirdMiddle.append(x)
        else:
            greater.append(x)

    return mySort(less)+pivot1+mySort(firstMiddle)+pivot2+mySort(middle)+pivot3+mySort(secondMiddle)+pivot4+mySort(thirdMiddle)+pivot5+mySort(greater)
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
