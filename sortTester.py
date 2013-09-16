##Author: Joshua Bloch
##
##This is a combination of two things:
##It is a list of every sort I've ever written, and some sorts I've pulled off the internet (rosettacode.org)
##It is also a sort tester. This serves two purposes:
##It can test your sort against any particular type of algorithm you'd like to test it against
##It also allows you to easily attempt to write a better version of any type of sort without having to write your own basic version first.
##To use it, import sortTester, then feed sortTester.sortTester a list of sorts you want it to test and a number (this number will become the length of the list it tests your sorts on)
##Alternatively, if you feed it "comprehension" instead of a number, it generates a leaderboard for list of length 10^1 to 10^7 by powers of ten.
import numpy.random as nprnd
import numpy as np
import random
from itertools import chain, repeat
from time import clock
import bisect
from collections import defaultdict
from bisect import bisect_left
from functools import total_ordering

def quickSortLambda(values):
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

def smedSort(values):
##    if len(values)<=1:
##        return values
    if len(values)<=14:
        for i in range(1,len(values)):
            value=values[i]
            hole=i
            while hole>0 and value<values[hole-1]:
                values[hole]=values[hole-1]
                hole-=1
            values[hole]=value
        return values
    pivot=[values[0],values[len(values)/2],values[-1]]
    pivot1=[min(pivot)]
    pivot.remove(pivot1[0])
    pivot2=[min(pivot)]
    pivot3=[max(pivot)]
    del values[len(values)/2], values[0], values[-1]
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
    less=smedSort(less)
    firstMiddle=smedSort(firstMiddle)
    secondMiddle=smedSort(secondMiddle)
    greater=smedSort(greater)

    return less+pivot1+firstMiddle+pivot2+secondMiddle+pivot3+greater

def smederSort(values):
##    if len(values)<=1:
##        return values
    if len(values)<=14:
        for i in range(1,len(values)):
            value=values[i]
            hole=i
            while hole>0 and value<values[hole-1]:
                values[hole]=values[hole-1]
                hole-=1
            values[hole]=value
        return values
    pivot=[values[0],values[len(values)/2],values[-1]]
    if pivot[0]>pivot[1]:
        pivot[0], pivot[1]=pivot[1],pivot[0]
    if pivot[0]>pivot[2]:
        pivot[0], pivot[2]=pivot[2],pivot[0]
    if pivot[1]>pivot[2]:
        pivot[1], pivot[2]=pivot[2],pivot[1]
    pivot1=[pivot[0]]
    pivot2=[pivot[1]]
    pivot3=[pivot[2]]
    del values[len(values)/2], values[0], values[-1]
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
    less=smedSort(less)
    firstMiddle=smedSort(firstMiddle)
    secondMiddle=smedSort(secondMiddle)
    greater=smedSort(greater)

    return less+pivot1+firstMiddle+pivot2+secondMiddle+pivot3+greater

def smedsSort(values):
    if len(values)<=1:
        return values
    if len(values)<=17:
        for i in range(1,len(values)):
            value=values[i]
            hole=i
            while hole>0 and value<values[hole-1]:
                values[hole]=values[hole-1]
                hole-=1
            values[hole]=value
        return values
    pivot=[values[0],values[1],values[2]]
    pivot1=[min(pivot)]
    pivot.remove(pivot1[0])
    pivot2=[min(pivot)]
    pivot3=[max(pivot)]
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

    less=smedsSort(less)
    firstMiddle=smedsSort(firstMiddle)
    secondMiddle=smedsSort(secondMiddle)
    greater=smedsSort(greater)

    return less+pivot1+firstMiddle+pivot2+secondMiddle+pivot3+greater

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
    return sorted(values)

def bubbleSort(values):
    for j in range (0, len(values)-1):
        for i in range(0,len(values)-1):
            if values[i]>values[i+1]:
                values[i],values[i+1]=values[i+1], values[i]
    return values

def combSort(values):
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
    return values

def cycleSort(values):
    writes=0
    for cycleStart in range(0,len(values)-1):
        item=values[cycleStart]
        pos=cycleStart
        for i in range(cycleStart+1,len(values)):
            if values[i]<item:
                pos+=1
        if pos==cycleStart:
            continue
        while item==values[pos]:
            pos+=1
        values[pos],item=item,values[pos]
        writes+=1
        while pos!=cycleStart:
            pos=cycleStart
            for i in range(cycleStart+1,len(values)):
                if values[i]<item:
                    pos+=1
            while item==values[pos]:
                pos+=1
            values[pos],item=item,values[pos]
            writes+=1
    return values

def dualPivotQuickSort(values):
    if len(values)<=1:
        return values
    pivot=[values[0],values[1]]
    pivot1=[min(pivot)]
    pivot2=[max(pivot)]
    del values[values.index(pivot1[0])]
    del values[values.index(pivot2[0])]
    less=[]
    middle=[]
    greater=[]
    for x in values:
        if x<=pivot1[0]:
            less.append(x)
        elif x>pivot1[0] and x<pivot2[0]:
            middle.append(x)
        else:
            greater.append(x)

    return dualPivotQuickSort(less)+pivot1+dualPivotQuickSort(middle)+pivot2+dualPivotQuickSort(greater)

def partialFlashSort(values):
    n=len(values)
    m=n/20
    l=[]
    for i in range (0,n):
        l.append(0)
    j=0
    k=0
    anmin=values[0]
    nmax=0
    for i in range(1,n):
        if values[i]<anmin:
            anmin=values[i]
        if values[i]>anmin:
            nmax=i
    if anmin==values[nmax]:
        return values
    c1=(float(m)-1)/(values[nmax]-anmin)
    for i in range(0,n):
        k=int(c1*(values[i]-anmin))
        l[k]+=1
    for k in range (1,m):
        l[k]+=l[k-1]
    hold=values[nmax]
    values[nmax]=values[0]
    values[0]=hold
    nmove=0
    k=m-1
    while nmove<n-1:
        while j>l[int(k)]-1:
            j+=1
            k=c1*(values[j]-anmin)
        flash=values[j]
        while j!=l[int(k)]:
            k=int(c1*(flash-anmin))
            hold=values[l[k]-1]
            values[int(l[k]-1)]=flash
            flash=hold
            l[k]-=1
            nmove+=1
    return values

def insertionSort(values):
    for i in range(1,len(values)):
        value=values[i]
        hole=i
        while hole>0 and value<values[hole-1]:
            values[hole]=values[hole-1]
            hole-=1
        values[hole]=value
    return values

def flashSort(values):
    values=partialFlashSort(values)
    values=insertionSort(values)
    return values

def heapify(values):
    start = (len(values) - 2) / 2
    while start >= 0:
        siftDown(values, start, len(values) - 1)
        start -= 1

def siftDown(values, start, end):
    root = start
    while root * 2 + 1 <= end:
        child = root * 2 + 1
        if child + 1 <= end and values[child] < values[child + 1]:
            child += 1
        if child <= end and values[root] < values[child]:
            values[root], values[child] = values[child], values[root]
            root = child
        else:
            return

def heapSort(values):
    heapify(values)
    end = len(values) - 1
    while end > 0:
        values[end], values[0] = values[0], values[end]
        siftDown(values,0, end - 1)
        end -= 1
    return values

def merge(left,right):
    result=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i=i+1
        else:
            result.append(right[j])
            j=j+1
    result=result+left[i:]
    result=result+right[j:]
    return result

def mergeSort(values):
    if len(values)<=1:
        return values
    middle=int( len(values)/2)
    left=mergeSort(values[:middle])
    right=mergeSort(values[middle:])
    return merge(left,right)

def quadPivotQuickSort(values):
    if len(values)<=1:
        return values
    if len(values)<=4:
        for i in range(1,len(values)):
            value=values[i]
            hole=i
            while hole>0 and value<values[hole-1]:
                values[hole]=values[hole-1]
                hole-=1
            values[hole]=value
        return values
    pivot=[values[0],values[1],values[2],values[3]]
    pivot1=[min(pivot)]
    pivot.remove(min(pivot))
    pivot2=[min(pivot)]
    pivot.remove(min(pivot))
    pivot3=[min(pivot)]
    pivot4=[max(pivot)]
    del values[0:4]
    less=[]
    firstMiddle=[]
    middle=[]
    secondMiddle=[]
    greater=[]
    for x in values:
        if x<=pivot1[0]:
            less.append(x)
        elif x>pivot1[0] and x<=pivot2[0]:
            firstMiddle.append(x)
        elif x>pivot2[0] and x<=pivot3[0]:
            middle.append(x)
        elif x>pivot3[0] and x<=pivot4[0]:
            secondMiddle.append(x)
        else:
            greater.append(x)

    return quadPivotQuickSort(less)+pivot1+quadPivotQuickSort(firstMiddle)+pivot2+quadPivotQuickSort(middle)+pivot3+quadPivotQuickSort(secondMiddle)+pivot4+quadPivotQuickSort(greater)

def quickSort(values):
    if len(values)<=1:
        return values
    pivot=[values[0],values[len(values)/2],values[-1]]
    pivot.remove(max(pivot))
    pivot.remove(min(pivot))
    values.remove(pivot[0])
    less=[]
    greater=[]
    for x in values:
        if x<pivot[0]:
            less.append(x)
        if x==pivot[0]:
            pivot.append(x)
        else:
            greater.append(x)

    return quickSort(less)+pivot+quickSort(greater)

def shellSort(values):
    gaps=[701,301,132,57,23,10,4,1]

    for gap in gaps:
        for i in range (gap, len(values)):
            temp=values[i]
            j=i
            while j>=gap and values[j-gap]>temp:
                values[j]=values[j-gap]
                j-=gap
            values[j]=temp
    return values

def selectionSort(values):
    q=[]
    x=values[:]
    for v in values:
        y=min(x)
        q.append(y)
        x.remove(y)
    return q

def gnomeSort(values):
    i,j=1,2
    while i<len(values):
        if values[i-1]<=values[i]:
            i,j=j,j+1
        else:
            values[i-1],values[i]=values[i],values[i-1]
            i-=1
            if i==0:
                i,j=j,j+1
    return values

def stoogesort(values,i,j):
    if values[j]<values[i]:
            values[i],values[j]=values[j],values[i]
    if j-i>1:
            t=(j-i+1)//3
            stoogesort(values,i,j-t)
            stoogesort(values,i+t,j)
            stoogesort(values,i,j-t)
    return values

def stoogeSort(values):
    i=0
    j=len(values)-1
    values=stoogesort(values,i,j)
    return values

def introSort(values):
    if len(values)<=1:
        return values
    if len(values)<=28:
        heapify(values)
        end = len(values) - 1
        while end > 0:
            values[end], values[0] = values[0], values[end]
            siftDown(values,0, end - 1)
            end -= 1
        return values
    pivot=[values[0],values[1],values[2]]
    pivot1=[min(pivot)]
    pivot.remove(pivot1[0])
    pivot2=[min(pivot)]
    pivot3=[max(pivot)]
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

    return introSort(less)+pivot1+introSort(firstMiddle)+pivot2+introSort(secondMiddle)+pivot3+introSort(greater)

def cardSort(values):
    sortedList=[]
    for i in range(min(values),max(values)+1):
        if i in values:
            for card in values:
                if card==i:
                    sortedList.append(card)
    return sortedList


def binSort(values):
    for value in xrange(1, len(values)):
        bisect.insort(values, values.pop(value), 0, value)
    return values


def sortTimer(sort,unsortedList):
    t1=clock()
    sort(unsortedList)
    t2=clock()
    return t2-t1

def sortTester(sorts, length):
    if length=='comprehension':
        sorts1=[]
        for i in range(len(sorts)):
            sorts1.append(0)
        for exponent in range(1,8):
            print "Testing on a list of length:", 10**exponent
            unsortedList=nprnd.randint(0,10**exponent,10**exponent).tolist()
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
                sorts1[place]=sorts[leader]
                del times[leader]
                del sorts[leader]
            sorts=sorts1[:]
            if exponent!=7:
                print ""
    else:    
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
    sorts=[timSort,reemSort]
    N=100000
    sortTester(sorts,N)

if __name__ == "__main__":
    main()
