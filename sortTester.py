import numpy.random as nprnd
import sortsList
from time import clock

def sortTimer(sort,unsortedList):
    t1=clock()
    sort(unsortedList)
    t2=clock()
    return t2-t1

def sortTester(sorts, length):
    unsortedList=nprnd.randint(0,length-1,length).tolist()
    times=[]
    for sort in sorts:
        times.append(sortTimer(sort,unsortedList))

    for place in range(len(times)):
        leader=times.index(min(times))
        if place==0:
            print '1st place:',sorts[leader].__name__,'took',times[leader],'seconds'
        elif place==1:
            print '2nd place:',sorts[leader].__name__,'took',times[leader],'seconds'
        elif place==2:
            print '3rd place:',sorts[leader].__name__,'took',times[leader],'seconds'
        else:
            print str(place+1)+'th place:',sorts[leader].__name__,'took',times[leader],'seconds'
        del times[leader]
        del sorts[leader]

def main():
    sorts=[sortsList.quickSort, sortsList.countSort, sortsList.smedserSort, sortsList.timSort, sortsList.reemSort, sortsList.quickSortNoLambdaBinarySort, sortsList.quickSortNoLambdaNonBinarySort, sortsList.binSort, sortsList.insertionSort, sortsList.flashSort]
    N=100000
    sortTester(sorts,N)

if __name__ == "__main__":
    main()
