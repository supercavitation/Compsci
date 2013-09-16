#Joshua Bloch
#2/12/13
#Roulette
import random
import time
players=int(raw_input('How many players? '))
dead=0
chamber=random.randint(1,6)
for i in range(1,players+1):
    if dead==0:
        if i==chamber:
            print 'Player', i, ', you died!'
            dead=1
        else:
            print 'Player', i, ', you survived!'
            time.sleep(2)
    else:
        print 'Player', i, ', you don\'t get a turn.'


