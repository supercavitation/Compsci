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
