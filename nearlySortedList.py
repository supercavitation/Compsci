import numpy.random as nprnd
from time import clock
 
def r_step_generator(lo, hi):
    num = lo
    while True:
        num += nprnd.randint(0, 100)
        if num < hi:
            yield num
        else:
            raise StopIteration
  	    
N = 10 ** 3
t1 = clock()
 
u = range(0, (N // 100) * 99)
x = nprnd.randint(0, N, N // 100)
 
for i_x, i_u in enumerate(r_step_generator(0, N)):
    u.insert(i_u, x[i_x-1])
 
t2 = clock()
print t2 - t1
q=0
for i in range (len(u)-2):
    if u[i]>u[i+1]:
        q+=1
print q
