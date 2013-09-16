#Joshua Bloch
#4/8/13
#list a list

user_input = raw_input('Enter a list of words: ')
list_of_words = user_input.split()
list_of_words.sort()
for word in list_of_words:
    print word
