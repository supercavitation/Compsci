from time import clock
import random

try:
  from itertools import zip_longest
except:
  try:
    from itertools import izip_longest
  except:
    zip_longest = lambda *args: map(None, *args)
 
def beadsort(l):
  return map(len, columns(columns([[1] * e for e in l])))
 
def columns(l):
  return [filter(None, x) for x in zip_longest(*l)]

N=10000
unsortedList=[]
for i in range(N):
    unsortedList.append(random.randint(0,N))
t1=clock()
sortedList=beadsort(unsortedList)
t2=clock()

print (t2-t1)
