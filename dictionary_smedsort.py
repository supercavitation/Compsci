import random
import time
import itertools

def dictSmedserSort(values):
    if len(values)<=1:
        return values
    
    if len(values)<=20:
        for i in range(1,len(values)):
            value=values[i]
            hole=i
            while hole>0 and value<values[hole-1]:
                values[hole]=values[hole-1]
                hole-=1
            values[hole]=value
        return values
    
    pivot={0:values[1],1:values[2],2:values[3]}
    if pivot[0]>pivot[1]:
        pivot[0], pivot[1]=pivot[1],pivot[0]
    if pivot[0]>pivot[2]:
        pivot[0], pivot[2]=pivot[2],pivot[0]
    if pivot[1]>pivot[2]:
        pivot[1], pivot[2]=pivot[2],pivot[1]
        
##    pivots2={1:pivot[1]}
##    pivots3={2:pivot[2]}
    
##    del pivot
    del values[0:3]
    
    less={}
    firstMiddle={}
    secondMiddle={}
    greater={}
    
    for x in values:
        if x<=pivot[0]:
            less.update({'a'+str(len(less)):x})
        elif x>pivot[0] and x<pivot[1]:
            firstMiddle.update({'b'+str(len(firstMiddle)):x})
        elif x>=pivot[1] and x<pivot[2]:
            secondMiddle.update({'c'+str(len(secondMiddle)):x})
        else:
            greater.update({'d'+str(len(greater)):x})

    less=dictSmedserSort(less)
    firstMiddle=dictSmedserSort(firstMiddle)
    secondMiddle=dictSmedserSort(secondMiddle)
    greater=dictSmedserSort(greater)
    
    less.update({'a'+str(len(less)):pivot[0]})
    firstMiddle.update({'b'+str(len(firstMiddle)):pivot[1]})
    secondMiddle.update({'c'+str(len(secondMiddle)):pivot[2]})
    
    return dict(less.items()+firstMiddle.items()+secondMiddle.items()+greater.items())

def smedserSort(values):
    if len(values)<=1:
        return values
    
    if len(values)<=20:
        for i in range(1,len(values)):
            value=values[i]
            hole=i
            while hole>0 and value<values[hole-1]:
                values[hole]=values[hole-1]
                hole-=1
            values[hole]=value
        return values
    
    pivot=[values[0],values[1],values[2]]
    if pivot[0]>pivot[1]:
        pivot[0], pivot[1]=pivot[1],pivot[0]
    if pivot[0]>pivot[2]:
        pivot[0], pivot[2]=pivot[2],pivot[0]
    if pivot[1]>pivot[2]:
        pivot[1], pivot[2]=pivot[2],pivot[1]
        
    pivot1=[pivot[0]]
    pivot2=[pivot[1]]
    pivot3=[pivot[2]]
    
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

    less=smedserSort(less)
    firstMiddle=smedserSort(firstMiddle)
    secondMiddle=smedserSort(secondMiddle)
    greater=smedserSort(greater)

    return less+pivot1+firstMiddle+pivot2+secondMiddle+pivot3+greater

N=10000
winCounter=[0,0]
for j in range (100):
    list=[]
    for i in range(0,N):
        list.append(random.randint(1,N-1))
    dict={}
    for i in range(0,N):
        dict.update({i:random.randint(1,N-1)})

    t1=time.clock()
    sortedList=dictSmedserSort(list)
    t2=time.clock()

    dictsmeds=t2-t1

    t1=time.clock()
    sortedList=smedserSort(dict)
    t2=time.clock()

    smeds=t2-t1
    if dictsmeds>smeds:
        winCounter[1]+=1
    if smeds>dictsmeds:
        winCounter[0]+=1

print winCounter


