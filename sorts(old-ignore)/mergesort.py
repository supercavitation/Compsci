from heapq import merge
 
def merge_sort(m):
    if len(m) <= 1:
        return m
 
    middle = len(m) / 2
    left = m[:middle]
    right = m[middle:]
 
    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))

lists=[6,4,3,6,2,5,39,92,85,2,49,5,29,4,6,-2,4]
lists=merge_sort(lists)
print lists
