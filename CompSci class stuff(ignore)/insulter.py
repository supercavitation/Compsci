#Joshua Bloch
#2/05/13
#Insulter
import random
raw_input('Enter your name: ')
insult1='Your mother wears a flea collar.'
insult2='Your brain would rattle in a flea\'s skull.'
insult3='The Doctor wouldn\'t bother to save you.'
insult4='Your sanity is very much in question.'
insult5='Your maggot-ridden corpse is worth more than you!'

choiceNumber=random.randint(1,5)

if choiceNumber==1:
    print insult1
elif choiceNumber==2:
    print insult2
elif choiceNumber==3:
    print insult3
elif choiceNumber==4:
    print insult4
else:
    print insult5
