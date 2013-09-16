#Joshua Bloch
#2/05/13
#Fortune Teller

color=raw_input('Pick red or blue: ')
number=int(raw_input('Pick a number from 1-4: '))

if color=='red':
    if number==1:
        print 'You will become an engineer.'
    elif number==2:
        print 'You will die old and alone.'
    elif number==3:
        print 'You will go bankrupt soon.'
    else:
        print 'You will fail all of your classes.'
else:
    if number==1:
        print 'You will become a CEO.'
    elif number==2:
        print 'You will live long and prosper.'
    elif number==3:
        print 'You will be much beloved by your peers.'
    else:
        print 'You will get into the college of your choice.'
