import random
import time
N=100000000

list=[]
for i in range(0,N):
    list.append(random.randint(1,N-1))

t1=time.clock()
sortedList=sorted(list)
t2=time.clock()

print t2-t1
