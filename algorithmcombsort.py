#Joshua Bloch
#4/12/13
#Sorting algorithm
import random
import time
N=100000
#function to sort a list
def mySort(values):
 #Insert code here to sort the list "values"
    gap=len(values)
    while gap!=1 or swapped!=False:
        gap=max(1,int(gap/1.247330950103979))
        i=0
        swapped=False
        while not i+gap>=len(values):
            if values[i]>values[i+gap]:
                values[i],values[i+gap]=values[i+gap],values[i]
                swapped=True
            i+=1
   
#You do not need to edit anything below this line
list = []
for i in range(0,N):
 list.append(random.randint(1,N-1))
copy = list[:]
#time the sorting routine
t1 = time.clock()
mySort(copy)
t2 = time.clock()
#make sure the list was sorted correctly
list.sort()
assert(list==copy) 
#print how long the function took to do the sort
print 'mySort took', t2-t1, 'seconds.'
