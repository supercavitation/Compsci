#Joshua Bloch
#4/12/13
#Sorting algorithm
import random
import time
N=100000
#function to sort a list
def mySort(values):
 #Insert code here to sort the list "values"
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

     heapify(values)
     end = len(values) - 1
     while end > 0:
        values[end], values[0] = values[0], values[end]
        siftDown(values,0, end - 1)
        end -= 1
#You do not need to edit anything below this line
list = []
for i in range(0,N):
 list.append(random.randint(1,N-1))
copy = list[:]
#time the sorting routine
t1 = time.clock()
mySort(copy)
t2 = time.clock()
#make sure the list was sorted correctly
list.sort()
assert(list==copy) 
#print how long the function took to do the sort
print 'mySort took', t2-t1, 'seconds.'
