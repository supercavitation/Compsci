#Joshua Bloch
#4/12/13
#Sorting algorithm
import random
import time
N=16000
#function to sort a list
def mySort(unsorted):
 #Insert code here to sort the list "values"
    items = len(unsorted)
    sortedBins = []
    while( len(unsorted) > 0 ):
        highest = float("-inf")
        newBin = []
        i = 0
        while( i < len(unsorted) ):
            if( unsorted[i] >= highest ):
                highest = unsorted.pop(i)
                newBin.append( highest )
            else:
                i=i+1
        sortedBins.append(newBin)
     
    sorted = []
    while( len(sorted) < items ):
        lowBin = 0
        for j in range( 0, len(sortedBins) ):
            if( sortedBins[j][0] < sortedBins[lowBin][0] ):
                lowBin = j
        sorted.append( sortedBins[lowBin].pop(0) )
        if( len(sortedBins[lowBin]) == 0 ):
            del sortedBins[lowBin]
    return sorted
#You do not need to edit anything below this line
list = []
for i in range(0,N):
 list.append(random.randint(1,N-1))
copy = list[:]
#time the smedsort routine
t1 = time.clock()
copy=mySort(copy)
t2 = time.clock()
#make sure the list was sorted correctly
list.sort()
assert(list==copy) 
#print how long the function took to do the sort
print 'smedSort took', t2-t1, 'seconds.'
