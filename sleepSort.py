from time import sleep
from time import clock
from threading import Timer
import numpy.random as numrnd
 
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

N=10
unsortedList=numrnd.randint(0,N,N).tolist()
print 'start'
t1=clock()
sortedList=beadsort(unsortedList)
t2=clock()

print t2-t1
print t2
