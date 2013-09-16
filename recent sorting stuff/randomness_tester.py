import time
import random
list=[]
for i in range (1,1000000):
    list.append(i)
list2=list[:]
list3=list[:]
t1=time.clock()
list.sort()
t2=time.clock()
print t2-t1
t1=time.clock()
list2.sort()
t2=time.clock()
print t2-t1
t1=time.clock()
list3.sort()
t2=time.clock()
print t2-t1
