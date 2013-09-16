#Joshua Bloch
#4/29/13
#Unit 6 demo writing files

#read in a file
fileName='APChemFlashcards.py'
file=open(fileName,'r')

#open output file
outputFile= 'capitalizedFile.txt'
outFile=open(outputFile, 'w')

for line in file:
    newLine=line.upper()
    outFile.write(newLine)

outFile.close()
