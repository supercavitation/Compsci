#Joshua Bloch
#4/29/13
#reversed words
fileName="word.txt"
file=open(fileName,"r")

outputFile= 'reversedWords.txt'
outFile=open(outputFile, 'w')

dictionary=[]
for line in file:
    dictionary.append(line)

dictionary.reverse()

for word in dictionary:
    outFile.write(word)
outFile.close()
