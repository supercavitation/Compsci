#Joshua Bloch
#4/12/13
#Sorting algorithm
import random
import time
N=160000
#function to sort a list
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
def mySort(values):
 #Insert code here to sort the list "values"
    if len(values)<=1:
        return values
    if len(values)<=28:
        values=partialFlashSort(values)
        values=insertionSort(values)
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

    return mySort(less)+pivot1+mySort(firstMiddle)+pivot2+mySort(secondMiddle)+pivot3+mySort(greater)
#You do not need to edit anything below this line
list = []
for i in range(0,N):
 list.append(random.randint(1,N))
copy = list[:]
#time the smedsort routine
t1 = time.clock()
copy=mySort(copy)
t2 = time.clock()
#make sure the list was sorted correctly
list.sort()
assert(list==copy) 
#print how long the function took to do the sort
print 'smedSort took', t2-t1, 'seconds.'
