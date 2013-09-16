LP=[1, 1, 3, 5, 9, 15, 25, 41, 67, 109, 177, 287, 465, 753, 1219, 1973, 3193, 5167, 8361, 13529, 21891, 35421, 57313, 92735, 150049, 242785, 392835, 635621, 1028457, 1664079, 2692537, 4356617, 7049155, 11405773, 18454929, 29860703, 48315633, 78176337, 126491971, 204668309, 331160281, 535828591, 866988873]

def numberOfTrailingZeros(p):
    p=list(bin(p))
    counter=0
    for i in range (1,len(p)+1):
        j=len(p)-i
        if p[j]==str(0):
            counter+=1
        else:
            break
    return counter

def shift(p,value):
    #>>
    p=list(bin(p))
    for i in range (1,value+1):
        j=len(p)-i
        if p[j]==str(0):
            del p[j]
    return ''.join(p)

def shift2(p,value):
    #<<
    for i in range(0,value):
        p+='0'
    return p

def sort(values,LP):
    lo=min(values)
    hi=max(values)
    head=lo
    p=1
    pshift=1
    while head<hi:
        if (p and 3)==3:
            sift(values,pshift,head,LP)
            p=int(shift(p,2))
            pshift+=2
        else:
            if LP[pshift-1]>=hi-head:
                trinkle(values,p,pshift,head,False,LP)
            else:
                sift(values,pshift,head,LP)
            if pshift==1:
                p=shift2(p,1)
                pshift-=1
            else:
                p=shift2(p,(pshift-1))
                pshift=1
        p|=1
        head+=1
    trinkle(values, p, pshift, head,False,LP)
    while pshift!=1 or p!=1:
        if pshift<=1:
            trail=numberofTrailingZeros(p)
            p=int(shift(p,trail))
            pshift+=trail
        else:
            p=shift2(p,2)
            p=p^7
            pshift-=2
            trinkle(values, shift(p,1),pshift+1,head-LP[pshift]-1,True,LP)
            trinkle(values, p, pshift,head-1, True, LP)
        head-=1
        
def sift(values,pshift, head, LP):
    val=values[head]
    while pshift>1:
        rt=head-1
        lf=head-1-LP[pshift-2]
        if val>=values[lf] and val>=values[rt]:
            break
        if values[lf]>=values[rt]:
            values[head]=values[lf]
            head=lf
            pshift-=1
        else:
            values[head]=values[rt]
            head=rt
            pshift-=2
    values[head]=val

def trinkle(values, p, pshift, head, isTrusty, LP):
    val=values[head]
    while p!=1:
        stepson=head-LP[pshift]
        if values[stepson]<=val:
            break
        if (not isTrusty) and pshift>1:
            rt=head-1
            lf=head-1-LP[pshift-2]
            if values[rt]>=values[stepson] or values[lf]>=values[stepson]:
                break
            values[head]=values[stepson]
            head=stepson
            trail=numberOfTrailingZeros(p)
            p=shift(p,trail)
            pshift+=trail
            isTrusty=False
        if not isTrusty:
            values[head]=val
            sift(values,pshift,head,LP)
                
