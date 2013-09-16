i,j=1,2
while i<len(values):
    if values[i-1]<=a[i]:
        i,j=j,j+1
    else:
        values[i-1],values[i]=values[i],values[i-1]
        i-=1
        if i==0:
            i,j=j,j+1
return values
