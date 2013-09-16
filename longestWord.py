#Joshua Bloch
#4/9/13
#longest word

user_input=raw_input('Enter a list of words: ')

list_of_words=user_input.split()

list_of_words.sort(key=len)

print list_of_words[-1]
