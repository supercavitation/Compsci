import random
list=[]
j=0
for i in range (1000000):
    list.append(random.randint(1,1000000))
for i in range (999999):
    if list[i]>list[i+1]:
        j+=1
print j
