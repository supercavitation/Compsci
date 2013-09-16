#Joshua Bloch
#4/29/13
#palindrome

def palindromeChecker(word):
    word=word.split()
    reversedWord=word.reverse()
    if reversedWord==word:
        return word

fileName="word.txt"
file=open(fileName,'r')

dictionary=[]
for line in file:
    line=line.strip()
    dictionary.append(line)

palindromes=[]
for word in dictionary:
    if palindromeChecker(word)==word:
        print word
        palindromes.append(word)
        

for line in palindromes:
    print line
print "done"
