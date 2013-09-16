#Joshua Bloch
#4/12/13
#Sorting algorithm
import random
import time
N=160000
#function to sort a list
def heapify(values):
    start = (len(values) - 2) / 2
    while start >= 0:
        siftDown(values, start, len(values) - 1)
        start -= 1

def siftDown(values, start, end):
    root = start
    while root * 2 + 1 <= end:
        child = root * 2 + 1
        if child + 1 <= end and values[child] < values[child + 1]:
            child += 1
        if child <= end and values[root] < values[child]:
            values[root], values[child] = values[child], values[root]
            root = child
        else:
            return
def mySort(values):
 #Insert code here to sort the list "values"
    if len(values)<=1:
        return values
    if len(values)<=28:
        heapify(values)
        end = len(values) - 1
        while end > 0:
            values[end], values[0] = values[0], values[end]
            siftDown(values,0, end - 1)
            end -= 1
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
 list.append(random.randint(1,N))
copy = list[:]
#time the smedsort routine
t1 = time.clock()
copy=mySort(copy)
t2 = time.clock()
#make sure the list was sorted correctly
list.sort()
assert(list==copy) 
#print how long the function took to do the sort
print 'smedSort took', t2-t1, 'seconds.'
