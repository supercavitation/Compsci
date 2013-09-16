from collection import defaultdict
def countsort(values,mini, maxi):
    count=defaultdict(int)
    for i in array:
        count[i]+=1
    result=[]
    for j in xrange(mini,maxi+1):
        result+=[j]*count[j]
    return result
