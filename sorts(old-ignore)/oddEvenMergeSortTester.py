import random
import time
def compare_and_swap(x, a, b):
    if x[a] > x[b]:
        x[a], x[b] = x[b], x[a]
    return x
 
def oddeven_merge(x, lo, hi, r):
    step = r * 2
    if step < hi - lo:
        oddeven_merge(x, lo, hi, step)
        oddeven_merge(x, lo + r, hi, step)
        for i in range(lo + r, hi - r, step):
            compare_and_swap(x, i, i + r)
    else:
        compare_and_swap(x, lo, lo + r)
    return x
 
def oddeven_merge_sort_range(x, lo, hi):
    """ sort the part of x with indices between lo and hi.
 
    Note: endpoints (lo and hi) are included.
    """
    if (hi - lo) >= 1:
        # if there is more than one element, split the input
        # down the middle and first sort the first and second
        # half, followed by merging them.
        mid = lo + ((hi - lo) / 2)
        oddeven_merge_sort_range(x, lo, mid)
        oddeven_merge_sort_range(x, mid + 1, hi)
        oddeven_merge(x, lo, hi, 1)
    return x

def oddeven_merge_sort(x):
    return oddeven_merge_sort_range(x, 0, len(x)-1)
    
data=[]
n=(2**15)
for i in range (0,n+1):
    number=random.randint(1,10)
    data.append(i*number)
t1=time.clock()
copy=oddeven_merge_sort(data)
t2=time.clock()
print t2-t1
