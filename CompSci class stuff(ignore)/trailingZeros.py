def numberOfTrailingZeros(p):
    p=bin(p)
    p=list(p)
    counter=0
    print p
    for i in range (1,len(p)+1):
        j=len(p)-i
        if p[j]==str(0):
            counter+=1
        else:
            break
    return counter

p=128
print bin(p)
print numberOfTrailingZeros(p)
