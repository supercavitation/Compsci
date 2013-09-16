#Joshua Bloch
#4/12/13
#Sorting algorithm
import random
import time
N=170000
#function to sort a list
def quicksort(A):
	A = rec_quicksort(A, 0, len(A))
	return A

def rec_quicksort(A, l, r):
	if ((r - l) < 2): 
		return A
	else:
		pivot_index = random.randint(l, r-1)
		A[l], A[pivot_index] = A[pivot_index], A[l]
		partition_results = partition(A, l, r)
		A = partition_results[0]
		l1 = l
		r1 = partition_results[1]-1
		l2 = r1 + 1
		r2 = r
		A = rec_quicksort(A, l1, r1)
		A = rec_quicksort(A, l2, r2)
		return A
	
def partition(A, l, r):
	p = A[l]
	i = l+1
	for j in range (l+1, r):
		if (A[j] < p):
			A[i], A[j] = A[j], A[i]
			i += 1
	A[l], A[i-1] = A[i-1], A[l]
	return A, i
    
def quickSort(values):
    if len(values)<=1:
        return values
    pivot=[values[0],values[len(values)/2],values[-1]]
    pivot.remove(max(pivot))
    pivot.remove(min(pivot))
    values.remove(pivot[0])
    less=[]
    greater=[]
    for x in values:
        if x<pivot[0]:
            less.append(x)
        if x==pivot[0]:
            pivot.append(x)
        else:
            greater.append(x)

    return quickSort(less)+pivot+quickSort(greater)

def qSort(L):
    return (qSort([y for y in L[1:] if y <  L[0]]) + 
            L[:1] + 
            qSort([y for y in L[1:] if y >= L[0]])) if len(L) > 1 else L
#You do not need to edit anything below this line
list = []
for i in range(0,N):
 list.append(random.randint(1,N-1))
copy = list[:]
#time the sorting routine
t1 = time.clock()
copy=qSort(copy)
t2 = time.clock()
print len(copy)
#make sure the list was sorted correctly
list.sort()
assert(list==copy) 
#print how long the function took to do the sort
print 'mySort took', t2-t1, 'seconds.'
