#Joshua Bloch
#4/12/13
#Sorting algorithm
import random
import time
N=100000
#function to sort a list
def merge(left,right):
    result=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i=i+1
        else:
            result.append(right[j])
            j=j+1
    result=result+left[i:]
    result=result+right[j:]
    return result

def mergesort(values):
    if len(values)<=1:
        return values
    middle=int( len(values)/2)
    left=mergesort(values[:middle])
    right=mergesort(values[middle:])
    return merge(left,right)
                    
#You do not need to edit anything below this line
list=[int(N*random.random()) for i in xrange(N)]
copy = list[:]
#time the sorting routine
t1 = time.clock()
copy=mergesort(copy)
t2 = time.clock()
#the list was sorted correctly
list.sort()
assert(list==copy) 
#print how long the function took to do the sort
print 'mySort took', t2-t1, 'seconds.'
