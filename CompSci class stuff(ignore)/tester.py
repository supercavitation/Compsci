#Joshua Bloch
#4/12/13
#Sorting algorithm
import random
import time
N=100000
#function to sort a list
def quicksort(A):
    
#You do not need to edit anything below this line
list = []
for i in range(0,N):
 list.append(random.randint(1,N-1))
copy = list[:]
#time the sorting routine
t1 = time.clock()
copy=quicksort(copy)
t2 = time.clock()
#the list was sorted correctly
list.sort()
assert(list==copy) 
#print how long the function took to do the sort
print 'mySort took', t2-t1, 'seconds.'
