import bisect
from time import clock
import numpy.random as numrnd

def insertion_sort_bin(seq):
    for i in range(1, len(seq)):
        bisect.insort(seq, seq.pop(i), 0, i)
    return seq

def insertionSort(values):
    for i in range(1,len(values)):
        value=values[i]
        hole=i
        while hole>0 and value<values[hole-1]:
            values[hole]=values[hole-1]
            hole-=1
        values[hole]=value
    return values

def insertion_sort_binary(seq):
    for i in range(1, len(seq)):
        key = seq[i]
        # invariant: ``seq[:i]`` is sorted        
        # find the least `low' such that ``seq[low]`` is not less then `key'.
        #   Binary search in sorted sequence ``seq[low:up]``:
        low, up = 0, i
        while up > low:
            middle = (low + up) // 2
            if seq[middle] < key:
                low = middle + 1              
            else:
                up = middle
        # insert key at position ``low``
        seq[:] = seq[:low] + [key] + seq[low:i] + seq[i + 1:]

N=1000000
lists=numrnd.randint(1,N,N).tolist()
copy=lists[:]
secondCopy=lists[:]
t1=clock()
lists1=insertion_sort_bin(lists)
t2=clock()
##lists2=insertionSort(copy)
##t3=clock()
##lists3=insertion_sort_binary(secondCopy)
##t4=clock()
print t2-t1,'seconds'
##print t3-t2,'seconds'
##print t4-t3,'seconds'
