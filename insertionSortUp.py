def insertionSortUp(values):
    for i in range(1,len(values)):
        value=values[i]
        hole=i
        while hole+1<len(values) and value>values[hole+1]:
            values[hole]=values[hole+1]
            hole+=1
        values[hole]=value
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

lists=[0,2,3,1,4,5,2,4,5,6,5,2,5]
lists1=insertionSortUp(lists)
print lists1
lists2=insertionSort(lists)
print lists
print lists2
