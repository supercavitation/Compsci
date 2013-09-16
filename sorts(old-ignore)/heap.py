import random
values=[]
n=50
for i in range (0,n+1):
    number=random.randint(1,10)
    values.append(i*number)
print 'start'
count=len(values)
def heapSort(values, count):
    heapify(values, count)
    end=count-1
    while end>0:
        firstNumber=values[end]
        secondNumber=values[0]
        values[0]=firstNumber
        values[end]=secondNumber
        end=end-1
        siftDown(values,0, end)
        
def heapify(values, count):
    start=(count-2)/2
    while start>=0:
        siftDown(values, start, count-1)
        start=start-1

def siftDown(values, start, end):
    root=start

    while (root*2)+1>=end:
        child= (root*2)+1
        swap=root
        if values[swap]<values[child]:
            swap=child
        if child+1<=end and values[swap]<values[child+1]:
            swap=child+1
        if swap!=root:
            firstNumber=values[swap]
            secondNumber=values[root]
            values[swap]=secondNumber
            values[root]=firstNumber
            root=swap

print heapSort(values, count)
