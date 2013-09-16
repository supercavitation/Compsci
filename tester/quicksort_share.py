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
