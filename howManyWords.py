#Joshua Bloch
#4/24/13
#how many words

fileName="word.txt"
file=open(fileName,"r")
dictionary=[]
for line in file:
    line=line.strip()
    dictionary.append(line)

for i in range (2,22):
    counter=0
    for word in dictionary:
        if len(word)==i:
            counter+=1
    print 'There are', counter, 'words of length', i, 'in the dictionary'
