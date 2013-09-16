def quickSort(values):
    if len(values)==1:
        return values
    if len(values)>1:
        pivot=values[1]
        left=0
        right=len(values)-1
        while left<=right:
            while values[left]<pivot:
                left+=1
            while values[right]>pivot:
                right-=1
            if left<=right:
                values[left], values[right]=values[right], values[left]
                left+=1
                right-=1
        quickSort(values[:right-1])
        quickSort(values[left:])
        return values

def partition(values, left, right, pivotIndex):
    pivotValue=values[pivotIndex]
    values[pivotIndex], values[right]=values[right], values[pivotIndex]
    storeIndex=left
    for i in xrange(left,right):
        if values[i]<pivotValue:
            values[i], values[storeIndex]=values[storeIndex], values[i]
            storeIndex+=1
    values[storeIndex], values[right]=values[right], values[storeIndex]
    return storeIndex

def quicksort(values,left,right):
    if len(values)==1:
        return values
    if len(values)>1:
        pivotIndex=1
        pivotNewIndex=partition(values,left,right,pivotIndex)
        quicksort(values,left,pivotNewIndex-1)
        quicksort(values,pivotNewIndex+1, right)

lists=[0,62,4,2,5,7,3,6,3,5,7,3,7,3,2,7,5,6,8,9,3,4,5]
lists1=lists[:]

quicksort(lists,0, len(lists)-1)
list2=sorted(lists)
print lists
assert lists==list2
