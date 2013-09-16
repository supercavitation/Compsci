#Joshua Bloch
#4/12/13
#Sorting algorithm
import random
import time
N=2048
#function to sort a list
def mySort(up,values):
 #Insert code here to sort the list "values"
    def bitonic_sort(up,values):
        if len(values)<=1:
            return values
        else:
            first=bitonic_sort(True, values[:len(values)/2])
            second=bitonic_sort(False, values[len(values)/2:])
            return bitonic_merge(up, first+second)

    def bitonic_merge(up,values):
        if len(values)==1:
            return values
        else:
            bitonic_compare(up, values)
            first= bitonic_merge(up, values[:len(values)/2])
            second=bitonic_merge(up, values[len(values)/2:])
            return first+second

    def bitonic_compare(up, values):
        dist= len(values)/2
        for i in range (dist):
            if (values[i]>values[i+dist])==up:
                values[i],values[i+dist]=values[i+dist],values[i]

    values.reverse()
           
#You do not need to edit anything below this line
list = []
for i in range(0,N):
 list.append(random.randint(1,N-1))
copy = list[:]
#time the sorting routine
t1 = time.clock()
mySort(False,copy)
t2 = time.clock()
#make sure the list was sorted correctly
list.sort()
assert(list==copy) 
#print how long the function took to do the sort
print 'mySort took', t2-t1, 'seconds.'
