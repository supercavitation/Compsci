#Joshua Bloch
#4/12/13
#Sorting algorithm
import random
import time
N=2
#function to sort a list
def mySort(values):
 #Insert code here to sort the list "values"

    def inOrder(values):
        for x in range (0, len(values)-1):
            if values[x]>values[x+1]:
                return False
            return True
            
    x=1
    while True:
        section=values[0:x]
        random.shuffle(section)
        if inOrder(section)==True:
            x+=1
            if x==len(values):
                break
        else:
            x=1
            
    return values
   
#You do not need to edit anything below this line
list = []
for i in range(0,N):
 list.append(random.randint(1,N-1))
copy = list[:]
#time the sorting routine
t1 = time.clock()
copy=mySort(copy)
print copy
t2 = time.clock()
#make sure the list was sorted correctly
list.sort()
assert(list==copy) 
#print how long the function took to do the sort
print 'mySort took', t2-t1, 'seconds.'
