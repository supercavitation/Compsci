for n in xrange(49):
    lower=0
    upper=0
    for i in range(1,n+1):
        lower+=i
    for i in range(n,50):
        upper+=i
    if lower==upper:
        print n
        break
