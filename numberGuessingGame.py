#Joshua Bloch
#2/14/13
#Guessing Game
import random
number=random.randint(1,100)
print 'Guess a number between 1 and 100.'
count=0
while True:
    guess=int(raw_input('Guess? '))
    count=count+1
    if guess==number:
        print 'You got it in',count,'tries!'
        break
    elif guess>number:
        print 'Too high.'
    else:
        print 'Too low.'
