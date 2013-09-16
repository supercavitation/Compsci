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
    if len(values)<=17:
        for i in range(1,len(values)):
            value=values[i]
            hole=i
            while hole>0 and value<values[hole-1]:
                values[hole]=values[hole-1]
                hole-=1
            values[hole]=value
        return values
    pivot=[values[0],values[1],values[2]]
    pivot1=[min(pivot)]
    pivot.remove(pivot1[0])
    pivot2=[min(pivot)]
    pivot3=[max(pivot)]
    del values[0:3]
    less=[]
    firstMiddle=[]
    secondMiddle=[]
    greater=[]
    for x in values:
        if x<=pivot1[0]:
            less.append(x)
        elif x>pivot1[0] and x<pivot2[0]:
            firstMiddle.append(x)
        elif x>=pivot2[0] and x<pivot3[0]:
            secondMiddle.append(x)
        else:
            greater.append(x)

    return mySort(less)+pivot1+mySort(firstMiddle)+pivot2+mySort(secondMiddle)+pivot3+mySort(greater)
#You do not need to edit anything below this line
list = []
for i in range(0,N):
 list.append(random.randint(1,N-1))
copy = list[:]
#time the smedsort routine
t1 = time.clock()
copy=mySort(copy)
t2 = time.clock()
#make sure the list was sorted correctly
t3=time.clock()
list.sort()
t4=time.clock()
#print how long the function took to do the sort
print 'smedSort took', t2-t1, 'seconds.'
print 'timsort took', t4-t3, 'seconds.'
print 'timsort was', (t2-t1)/(t4-t3), 'times faster.' 
