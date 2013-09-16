q=[]
y=[]
x=[]
for i in range(0,10):
    x.append(i)
for i in range(1,11):
    y.append(0)
for i in range(0,9):
    q.append(y)
q.append(x)
for i in range (1,11):
    x=1
    c=0
    while True:
        if i-1>=0 and c<10:
            if q[i-1][c]:
                if c-1>=0:
                    if x>q[i-1][c-1]:
                        q[i-1][c]=x
        x+=1
        c+=1
        if c==10:
            break

for i in range(0,10):
    print q[i]
