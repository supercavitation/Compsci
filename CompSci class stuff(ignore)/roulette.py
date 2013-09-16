var =1
while var ==1:
    import random
    roulette=int(raw_input('How many players do you want to have out of 6?'))
    bullets=roulette
    while bullets>0:
        if roulette==6:
            print 'You died... idiot.'
            deaths=1
            break
        elif roulette>6:
            print 'How the hell???'
            deaths=1
            break
        elif random.randint(1,6)==roulette:
            print 'You died!'
            deaths=1
            break
        else:
            bullets-=1
            deaths=0
    if deaths==0:
        print 'You survived!'
    count=int(raw_input('Press 0 to exit, or 1 to continue.'))
    if count==0:
        break
