import random
from time import clock

def library_sort(array, epsilon):
 
    def binary_search(array, element, start, end):        
        mid = start + ((end-start)//2)
        if start == end:
            if array[mid] is not None and array[mid] <= element: return mid + 1
            else: return mid
        else:
            m = mid
            while m < end and array[m] is None: m += 1
            if m == end:
                if array[m] is not None and array[m] <= element: return m + 1
                else: return binary_search(array, element, start, mid)
            elif m == start:
                if array[m] > element: return m
                else: return binary_search(array, element, m+1, end)
            else:
                if array[m] == element: return m + 1
                elif array[m] > element: return binary_search(array, element, start, m-1)
                else: return binary_search(array, element, m+1, end)
 
    def insert(array, element, index):
        nonlocal last_insert_index
        if array[index] is None:
            array[index] = element
        else:
            while array[index] is not None:
                array[index], element = element, array[index]
                index += 1
            array[index] = element
            index += 1
        if index > last_insert_index:
                last_insert_index = index
 
    def balance(array, num_spaces, total_inserted):
        nonlocal last_insert_index
        queue = [None] * len(array)
        inserted = index = 1
        top = bottom = 0
 
        while inserted < total_inserted:
            spaces = 0
            while spaces < num_spaces:
                if array[index] is not None:
                    queue[bottom] = array[index]
                    bottom += 1
                array[index] = None
                index += 1; spaces += 1
            if array[index] is not None:
                queue[bottom] = array[index]
                bottom += 1
            array[index] = queue[top]
            index += 1; top += 1; inserted += 1
 
        last_insert_index = index - 1
 
 
    array_len = len(array)
    copy = [None] * (1 + epsilon) * array_len
    copy[0] = array[0]
    last_insert_index = 0
    inserted = index = 1
 
    while inserted < array_len:
        round_inserts = inserted
 
        while inserted < array_len and round_inserts > 0:
            insertion_index = binary_search(copy, array[index], 0, last_insert_index)
            insert(copy, array[index], insertion_index)
            round_inserts -= 1; inserted += 1; index += 1
        balance(copy, epsilon, inserted)
 
    return [x for x in copy if x is not None]

def insertionSort(values):
    for i in range(1,len(values)):
        value=values[i]
        hole=i
        while hole>0 and value<values[hole-1]:
            values[hole]=values[hole-1]
            hole-=1
        values[hole]=value
    return values

N=100000
unsortedList=[]
for i in range(N+1):
    unsortedList.append(random.randint(0,N))
t1=clock()
sortedList=library_sort(unsortedList,1)
t2=clock()
##secondSortedList=insertionSort(unsortedList)
t3=clock()
print(t2-t1)
print(t3-t2)
