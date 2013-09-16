def neighbours(baseList, list, j):
    counter=0
    if list-1>=0:
        if baseList[list-1][j]==1:
            counter+=1
        if j+1<=9:
            if baseList[list-1][j+1]==1:
                counter+=1
        if j-1>=0:
            if baseList[list-1][j-1]==1:
                counter+=1
    if list+1<=9:
        if baseList[list+1][j]==1:
            counter+=1
        if j+1<=9:
            if baseList[list+1][j+1]==1:
                counter+=1
        if j-1>=0:
            if baseList[list+1][j-1]==1:
                counter+=1
    if j+1<=9:
        if baseList[list][j+1]==1:
            counter+=1
    if j-1>=0:
        if baseList[list][j-1]==1:
            counter+=1
    return counter


baseList=[]
for i in range (0,10):
    baseList.append([0,1,1,0,0,0,0,0,0,0])

def iteration(neighborCounter,baseList):
    for list in range (0,10):
        for j in range (0,10):
            counter=neighborCounter[list][j]
            if baseList[list][j]==1 and counter<2:
                baseList[list][j]=0
            elif baseList[list][j]==1 and counter>3:
                baseList[list][j]=0
            elif baseList[list][j]==0 and counter==3:
                baseList[list][j]=1
    return baseList

neighborCounter=[]
for list in range(0,10):
    nextList=[]
    for j in range(0,10):
        nextList.append(neighbours(baseList,list,j))
    neighborCounter.append(nextList)

iterate=iteration(neighborCounter,baseList)

for list in range (0,10):
        print neighborCounter[list]
print ''
for list in range (0,10):
        print iterate[list]
        
