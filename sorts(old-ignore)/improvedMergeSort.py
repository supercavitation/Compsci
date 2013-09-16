#Joshua Bloch
#4/12/13
#Sorting algorithm
import random
import time
N=100
#function to sort a list
def merge(left,right):
    result=[]
    i,j,k=0,0,0
    while i<len(left) and j<len(right):
        if left[i]<=right[j] and len(left)>1:
            while i+k<len(left) and left[i+k]<=right[j]:
                k+=1
            for x in range(i,i+k):
                result.append(left[x])
            i=i+k
            k=0
        elif left[i]<=right[j] and len(left)==1:
            result.append(left[i:i+k+1])
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
list = []
for i in range(0,N):
 list.append(random.randint(1,N-1))
copy = list[:]
#time the sorting routine
t1 = time.clock()
copy=mergesort(copy)
t2 = time.clock()
#the list was sorted correctly
list.sort()
print copy
print len(copy)
assert(list==copy) 
#print how long the function took to do the sort
print 'mySort took', t2-t1, 'seconds.'
