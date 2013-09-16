import random
import time
values=[]
n=100000
def mySort(values):
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
    del values[values.index(pivot1[0])]
    del values[values.index(pivot2[0])]
    del values[values.index(pivot3[0])]
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

    return mySort(less)+pivot1+mySort(firstMiddle)+pivot2+mySort(secondMiddle)+pivot3+mySort(greater)

for i in range(0,n):
    values.append(i)
print 'Start'
t1=time.clock()
copy=mySort(values)
t2=time.clock()
print 'Next'
q=0
for x in range (0,len(copy)-2):
    if copy[x]>copy[x+1]:
        q=q+1
if q==0:
    print "This algorithm took", t2-t1, "seconds to sort", n, "terms."
