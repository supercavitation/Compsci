#Joshua Bloch
#1/30/13
#stringAnalysis

sentence=raw_input('Enter a sentence: ')
wordNumber=int(sentence.count(' '))
characterNumber=int(len(sentence))
letterNumber=characterNumber-wordNumber

print ('Your sentence has'), wordNumber+1, ('words,'), characterNumber, ('characters and'), letterNumber, ('letters.')
searchCharacter=raw_input ('Enter a character to search for: ')
characterOccurance=sentence.count (searchCharacter)
print ('Your sentence has'), characterOccurance, ('of the character'), searchCharacter, ('.')
searchWord=raw_input ('Enter a word to search for: ')
wordOccurance=sentence.count (searchWord)
print ('Your sentence has'), wordOccurance, ('of the word'), searchWord, ('.')
