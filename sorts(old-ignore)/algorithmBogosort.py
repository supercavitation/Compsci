#Joshua Bloch
#4/12/13
#Sorting algorithm
import random
import time
N=58
#function to sort a list
def mySort(values):
 #Insert code here to sort the list "values"
    def inOrder(values):
        x=0
        if values[x]>values[x+1]:
            return False
        else:
            return True
        
    while not inOrder(values):
        x=len(values)
        q,y=[],[]
        for i in values:
            q.append(i)
        for z in values:
            w=random.randint(0,len(q))
            y.append(values[w])
            q.remove(values.index(w))
        
    return values
   
#You do not need to edit anything below this line
list = []
for i in range(0,N):
 list.append(random.randint(1,N-1))
copy = list[:]
#time the sorting routine
t1 = time.clock()
copy=mySort(copy)
t2 = time.clock()
#make sure the list was sorted correctly
list.sort()
assert(list==copy) 
#print how long the function took to do the sort
print 'mySort took', t2-t1, 'seconds.'
