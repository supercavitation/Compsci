#Joshua Bloch
#4/29/13
#anagram
fileName="word.txt"
file=open(fileName,"r")

word=raw_input('Enter a word: ')

dictionary=[]
for line in file:
    line=line.strip()
    dictionary.append(line)

for char in word:
    for line in dictionary:
        if char not in line:
            dictionary.remove(line)
    
for line in dictionary:
    if len(word)!=len(line):
        dictionary.remove(line)

for line in dictionary:
    print line

print 'done'
