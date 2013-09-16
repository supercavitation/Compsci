#Joshua Bloch
#4/12/13
#Sorting algorithm
import random
import time
N=135000
#function to sort a list
def mySort(values):
 #Insert code here to sort the list "values"
    import heapq
    for x in range(0,len(values)):
        values[x]=values[x]*-1
    heapq.heapify(values)
    for x in range(0,len(values)):
        values[x]=values[x]*-1
    heapq.heapify(values)
    for x in range(0,len(values)):
        while values[x]<values[x-1]:
            values[x-1],values[x]=values[x],values[x-1]
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
