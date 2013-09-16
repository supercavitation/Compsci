
def bitonic_sort(up,values):
    in len[values]<=1:
        return values
    else:
        first=bitonic_sort(True, values[:len(values)/2])
        second=bitonic_sort(False, values[len(values)/2:])
        return bitonic_merge(up, first+second)

def bitonic_merge(up,values):
    if len(values)==1:
        return values
    else:
        bitonic_compare(up, values)
        first= bitonic_merge(up, values[:len(values)/2])
        second=bitonic_merge(up, values[len(values)/2:])
        return first+second

def bitonic_compare(up, values):
    dist= len(values)/2
    for i in range (dist):
        if (values[i]>x[i+dist])==up:
            x[i],x[i+dist]=x[i+dist],x[i]
    
