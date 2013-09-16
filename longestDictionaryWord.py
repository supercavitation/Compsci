#Joshua Bloch
#4/24/13
#longest word in the Dictionary

fileName="words.txt"
file=open(fileName,"r")
dictionary=[]
for line in file:
    line=line.strip()
    dictionary.append(line)
dictionary.sort(key=len)
print dictionary[-1]
