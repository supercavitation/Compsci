import random
numberList=[]
n=5000
for i in range (0,n+1):
    number=random.randint(1,10)
    numberList.append(i*number)
print 'start'
def heapify(numberList):
    for i in range (0, len(numberList)):
        for i in range (0,len(numberList)/2):
            i=(len(numberList)/2)-i
            maxHeap(numberList,i)
    return numberList

def maxHeap(numberlist,i):
    left=2*i+1
    right=2*i+2
    largest=i
    if left<len(numberList) and numberList[left]>numberList[largest]:
        largest=left
    if right<len(numberList) and numberList[right]>numberList[largest]:
        largest=right
    if largest!=i:
        number1=numberList[i]
        number2=numberList[largest]
        numberList[i]=number2
        numberList[largest]=number1
        maxHeap(numberList, largest)
   
print heapify(numberList)
        
            
            
