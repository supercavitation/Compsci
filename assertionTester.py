#Joshua Bloch
#4/12/13
#Sorting algorithm
import random
import time
N=5000
#function to sort a list
def mySort(values):
    import math
 #Insert code here to sort the list "values"

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
