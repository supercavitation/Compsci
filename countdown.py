#Joshua Bloch
#2/12/13
#countdown
import time
for i in range (1,7):
    if i<6:
        print 6-i
        time.sleep(1)
    else:
        print 'BOOM!'
