#Joshua Bloch
#2/28/13
#multiplier

import random

counter=0

def complementer():
    complement=random.randint(1,5)
    if complement==1:
        print 'Nice job, you\'re doing great!'
    elif complement==2:
        print 'Keep up the amazing work!'
    elif complement==3:
        print 'You\'re a pro!'
    elif complement==4:
        print 'You\'re owning these problems!'
    else:
        print 'You\'ll be top of the class in no time!'

while True:
    firstTerm=random.randint(1,12)
    secondTerm=random.randint(1,12)
    answer=firstTerm*secondTerm
    print str(firstTerm)+'x'+str(secondTerm)+'='
    guess=int(raw_input('? '))
    if guess==answer:
        counter=counter+1
    else:
        print 'Sorry, that\'s not correct.'
    if counter==5:
        complementer()
        counter=0
