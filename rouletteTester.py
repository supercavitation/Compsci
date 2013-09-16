import random
for j in range(1,101):
    dead=0
    chamber=random.randint(1,6)
    for i in range(1,7):
        if dead==0:
            if i==chamber:
                print 'Player', i, ', you died!'
                dead=1
            else:
                print 'Player', i, ', you survived!'
        else:
            print 'Player', i, ', you don\'t get a turn.'
