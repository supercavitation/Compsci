import numpy.random as nprnd
import numpy as np
import random
from itertools import chain, repeat
from time import clock
import bisect
from collections import defaultdict

def quickSort(values):
##    if len(values)<=1:
##        return values
    if len(values)<=13:
        for i in range(1,len(values)):
            value=values[i]
            hole=i
            while hole>0 and value<values[hole-1]:
                values[hole]=values[hole-1]
                hole-=1
            values[hole]=value
        return values
    
    pivotsList=random.sample(values,2)

    if pivotsList[0]>pivotsList[1]:
        pivotsList[0], pivotsList[1]=pivotsList[1],pivotsList[0]
        
    lowerList=[]
    middleList=[]
    upperList=[]
    
    lowerList = filter(lambda value: pivotsList[0]>=value, values)
    middleList = filter(lambda value: pivotsList[0]<value<=pivotsList[1], values)
    upperList = filter(lambda value: pivotsList[1]<value, values)

    lowerList=quickSort(lowerList)
    middleList=quickSort(middleList)
    upperList=quickSort(upperList)

##    lowerList.append(pivotsList[0])
##    lowerMiddleList.append(pivotsList[1])
##    upperMiddleList.append(pivotsList[2])

    sortedList=list(chain(lowerList,middleList,upperList))

    return sortedList

def quickSortNoLambdaNonBinarySort(values):
    if len(values)==1:
        return values
    
    if len(values)==2:
        if values[0]>values[1]:
            values[0],values[1]=values[1],values[0]
        return values
    
    if len(values)==3:
        if values[0]>values[1]:
            values[0], values[1]=values[1],values[0]
        if values[0]>values[2]:
            values[0], values[2]=values[2],values[0]
        if values[1]>values[2]:
            values[1], values[2]=values[2],values[1]
        return values
    
    if len(values)<=19:
        for i in xrange(1,len(values)):
            value=values[i]
            hole=i
            while hole>0 and value<values[hole-1]:
                values[hole]=values[hole-1]
                hole-=1
            values[hole]=value
        return values
    
    pivotsList=random.sample(values,2)

    if pivotsList[0]>pivotsList[1]:
        pivotsList[0], pivotsList[1]=pivotsList[1],pivotsList[0]
        
    lowerList=[]
    middleList=[]
    upperList=[]
    
    for value in values:
        if value<=pivotsList[0]:
            lowerList.append(value)
        elif value<=pivotsList[1]:
            middleList.append(value)
        else:
            upperList.append(value)

    lowerList=quickSortNoLambdaNonBinarySort(lowerList)
    middleList=quickSortNoLambdaNonBinarySort(middleList)
    upperList=quickSortNoLambdaNonBinarySort(upperList)

    sortedList=lowerList+middleList+upperList

    return sortedList

def quickSortNoLambdaBinarySort(values):
    if len(values)==1:
        return values
    
    if len(values)==2:
        if values[0]>values[1]:
            values[0],values[1]=values[1],values[0]
        return values
    
    if len(values)==3:
        if values[0]>values[1]:
            values[0], values[1]=values[1],values[0]
        if values[0]>values[2]:
            values[0], values[2]=values[2],values[0]
        if values[1]>values[2]:
            values[1], values[2]=values[2],values[1]
        return values
    
    if len(values)<=21:
        for value in xrange(1, len(values)):
            bisect.insort(values, values.pop(value), 0, value)
        return values
    
    pivotsList=random.sample(values,2)

    if pivotsList[0]>pivotsList[1]:
        pivotsList[0], pivotsList[1]=pivotsList[1],pivotsList[0]
        
    lowerList=[]
    middleList=[]
    upperList=[]
    
    for value in values:
        if value<=pivotsList[0]:
            lowerList.append(value)
        elif value<=pivotsList[1]:
            middleList.append(value)
        else:
            upperList.append(value)

    lowerList=quickSortNoLambdaBinarySort(lowerList)
    middleList=quickSortNoLambdaBinarySort(middleList)
    upperList=quickSortNoLambdaBinarySort(upperList)

    sortedList=lowerList+middleList+upperList

    return sortedList

def countSort(values):
    count=defaultdict(int)
    for i in values:
        count[i]+=1
    result=[]
    for j in xrange(min(count), max(count)+1):
        result+=[j]*count[j]
    return result

def reemSort(unsorted_list):
    counts = (np.bincount(np.array(unsorted_list))).tolist()

    sorted_list = list(
        chain.from_iterable(
            repeat(num, counts[num])
            for num in xrange(len(counts))))

    return sorted_list

def smedserSort(values):
    if len(values)<=1:
        return values
    if len(values)<=20:
        for i in range(1,len(values)):
            value=values[i]
            hole=i
            while hole>0 and value<values[hole-1]:
                values[hole]=values[hole-1]
                hole-=1
            values[hole]=value
        return values
    pivot=[values[0],values[1],values[2]]
    if pivot[0]>pivot[1]:
        pivot[0], pivot[1]=pivot[1],pivot[0]
    if pivot[0]>pivot[2]:
        pivot[0], pivot[2]=pivot[2],pivot[0]
    if pivot[1]>pivot[2]:
        pivot[1], pivot[2]=pivot[2],pivot[1]
    pivot1=[pivot[0]]
    pivot2=[pivot[1]]
    pivot3=[pivot[2]]
    del values[0:3]
    less=[]
    firstMiddle=[]
    secondMiddle=[]
    greater=[]
    for x in values:
        if x<=pivot1[0]:
            less.append(x)
        elif x>pivot1[0] and x<pivot2[0]:
            firstMiddle.append(x)
        elif x>=pivot2[0] and x<pivot3[0]:
            secondMiddle.append(x)
        else:
            greater.append(x)

    less=smedserSort(less)
    firstMiddle=smedserSort(firstMiddle)
    secondMiddle=smedserSort(secondMiddle)
    greater=smedserSort(greater)

    return less+pivot1+firstMiddle+pivot2+secondMiddle+pivot3+greater

def timSort(values):
    values=sorted(values)
    return values

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
    sorts=[quickSort, countSort, smedserSort, timSort, reemSort, quickSortNoLambdaBinarySort, quickSortNoLambdaNonBinarySort]
    N=100000
    sortTester(sorts,N)

if __name__ == "__main__":
    main()
