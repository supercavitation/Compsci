#Joshua Bloch
#4/9/13
#statistics

def median(numberList):
    return numberList[len(numberList)/2]

def mode(numberList):
    frequencyList=[]
    for number in numberList:
        frequencyList.append(numberList.count(number))
    return numberList[frequencyList.index(max(frequencyList))]

numberList=[]
total=0
while True:
    number=raw_input('')
    if number=='q':
        break
    else:
        numberList.append(float(number))
for number in numberList:
    total=total+number
print 'Min:', min(numberList)
print 'Mean:', total/len(numberList)
print 'Median:', median(numberList)
print 'Max:', max(numberList)
print 'Mode:', mode(numberList)

