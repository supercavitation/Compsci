num=0
for i in range(10):
    for j in range(10):
        if ((i*10^6)+345670+j)%11==0:
            num+=1
print(num)
