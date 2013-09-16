for a in range(10):
    a=float(a)
    for b in range(10):
        b=float(b)
        for c in range(1,10):
            c=float(c)
            if (b*10+c)!=0:
                if (a*10+b)/(b*10+c)==(a/c):
                    if (a*10+b)%11!=0 or (b*10+c)%11!=0:
                        if (a*10+b)/(b*10+c)!=0:
                            print str(int(a*10+b))+'/'+str(int(b*10+c)), str(int(a))+'/'+str(int(c))
print 'done'
                                

