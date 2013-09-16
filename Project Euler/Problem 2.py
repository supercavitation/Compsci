list1=[0,1]
i=1
j=0
while list1[i]<=4000000:
    list1.append(list1[i-1]+list1[i])
    i+=1
for term in range(len(list1)):
    if list1[term]%2==0:
        j+=list1[term]
print j
