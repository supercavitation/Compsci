#Joshua Bloch
#4/12/13
#Sorting algorithm
import random
import time
N=100000
#function to sort a list
def mySort(values):
 #Insert code here to sort the list "values"
    gaps=[701,301,132,57,23,10,4,1]

    for gap in gaps:
        for i in range (gap, len(values)):
            temp=values[i]
            j=i
            while j>=gap and values[j-gap]>temp:
                values[j]=values[j-gap]
                j-=gap
            values[j]=temp
       
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
