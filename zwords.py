#Joshua Bloch
#4/29/13
#zwords

fileName="word.txt"
file=open(fileName,"r")

outputFile= 'zwords.txt'
outFile=open(outputFile, 'w')

dictionary=[]
for line in file:
    dictionary.append(line)

zwords=[]
for word in dictionary:
    if 'z' in word:
        zwords.append(word)

for word in zwords:
    outFile.write(word),
outFile.close()

