#Joshua Bloch
#4/12/13
#Sorting algorithm
import random
import time
N=1000
#function to sort a list
def stoogesort(values,i,j):
    if values[j] < values[i]:
            values[i], values[j] = values[j], values[i]
    if j - i > 1:
            t = (j - i + 1) // 3
            stoogesort(values, i  , j-t)
            stoogesort(values, i+t, j  )
            stoogesort(values, i  , j-t)
    return values
                    
#You do not need to edit anything below this line
list = []
for i in range(0,N):
 list.append(random.randint(1,N-1))
copy = list[:]
#time the sorting routine
t1 = time.clock()
copy=stoogesort(copy,0,len(copy)-1)
t2 = time.clock()
#the list was sorted correctly
list.sort()
assert(list==copy) 
#print how long the function took to do the sort
print 'mySort took', t2-t1, 'seconds.'
