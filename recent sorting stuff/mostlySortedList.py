import numpy.random as random
from time import clock

N=10000000
u=[]
t1=clock()
for x in range(0,N/100+1):
    for y in range (0,100):
        u.append(x*100+y)
    u.append(random.randint(1,N))
t2=clock()
print t2-t1
