import random
values=[]
n=10
for i in range (0,n+1):
    number=random.randint(1,10)
    values.append(i*number)
print 'start'
def merge_sort(values):
    if len(values)<=1:
        return values
    left=[]
    right=[]
    middle=len(values)/2
    left.append(values[0:middle])
    right.append(values[middle+1:])
    left=merge_sort(left)
    right=merge_sort(right)
    return merge(left, right)

def merge(left, right):
    result=[]
    while len(left)>0 or len(right)>0:
        if len(left)>0 and len(right)>0:
            if left[0]<=right[0]:
                result.append(left[0])
                left.remove(left[0])
            else:
                result.append(right[0])
                right.remove(right[0])
        elif len(left)>0:
            result.append(left[0])
            left.remove(left[0])
        else:
            result.append(right[0])
            right.remove(right[0])
    return result
    
copy=merge_sort(values)
print copy
if merge_sort(values)==values.sort():
    print True
