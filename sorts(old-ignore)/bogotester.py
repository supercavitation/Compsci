import random
import time
values=[]
n=100000
for i in range (0,n):
    number=random.randint(1,10)
    values.append(i*number)
print 'start'
def bogosort(values):
    import heapq
    for x in range(0,len(values)):
        values[x]=values[x]*-1
    heapq.heapify(values)
    for x in range(0,len(values)):
        values[x]=values[x]*-1
    heapq.heapify(values)
    for x in range(0,len(values)):
        insert=values[x]
        hole=x
        while hole>0 and insert<values[hole-1]:
            values[hole]=values[hole-1]
            hole-=1
        values[hole]=insert
    return values

t1=time.clock()
copy=bogosort(values)
t2=time.clock()
print "This algorithm took", t2-t1, "seconds to sort", n, "terms."
