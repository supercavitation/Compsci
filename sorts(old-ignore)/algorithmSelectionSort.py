#Joshua Bloch
#4/12/13
#Sorting algorithm
import random
import time
N=100
#function to sort a list
def mySort(values):
 #Insert code here to sort the list "values"
    sortedList=[]
    while len(values)!=0:
        firstNumber=values[0]
        index=0
        for i in range (0, len(values)-2):
            if values[i+1]<values[i]:
                firstNumber=values[i+1]
                index=i+1
        sortedList.append(firstNumber)
        del values[index]
    return sortedList
   
#You do not need to edit anything below this line
list = []
for i in range(0,N):
 list.append(random.randint(1,N-1))
copy = list[:]
#time the sorting routine
t1 = time.clock()
copy=mySort(copy)
t2 = time.clock()
print copy
#make sure the list was sorted correctly
list.sort()
assert(list==copy) 
#print how long the function took to do the sort
print 'mySort took', t2-t1, 'seconds.'
