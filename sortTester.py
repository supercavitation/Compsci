##Author: Joshua Bloch
##
##This is a combination of two things:
##It is a list of every sort I've ever written, and some sorts I've pulled off the internet (rosettacode.org)
##It is also a sort tester. This serves two purposes:
##It can test your sort against any particular type of algorithm you'd like to test it against
##It also allows you to easily attempt to write a better version of any type of sort without having to write your own basic version first.
##To use it, import sortTester, then feed sortTester.sortTester a list of sorts you want it to test and a number (this number will become the length of the list it tests your sorts on)
##Alternatively, if you feed it "powers of ten" instead of a number, it generates a leaderboard for list of length 10^1 to 10^7 by powers of ten.
import numpy.random as nprnd
import sortList

def sortTimer(sort,unsortedList):
    t1=clock()
    sort(unsortedList)
    t2=clock()
    return t2-t1

def sortTester(sorts, length):
    if length=='powers of ten':
        sorts1=[]
        for i in range(len(sorts)):
            sorts1.append(0)
        for exponent in range(1,8):
            print "Testing on a list of length:", 10**exponent
            unsortedList=nprnd.randint(0,10**exponent,10**exponent).tolist()
            times=[]
            for sort in sorts:
                times.append(sortTimer(sort,unsortedList))

            for place in range(len(times)):
                leader=times.index(min(times))
                if place==0:
                    print '1st place:',sorts[leader].__name__,'took',times[leader],'seconds'
                elif place==1:
                    print '2nd place:',sorts[leader].__name__,'took',times[leader],'seconds'
                elif place==2:
                    print '3rd place:',sorts[leader].__name__,'took',times[leader],'seconds'
                else:
                    print str(place+1)+'th place:',sorts[leader].__name__,'took',times[leader],'seconds'
                sorts1[place]=sorts[leader]
                del times[leader]
                del sorts[leader]
            sorts=sorts1[:]
            if exponent!=7:
                print ""
    else:
        print "Testing on a list of length:", length 
        unsortedList=nprnd.randint(0,length-1,length).tolist()
        times=[]
        for sort in sorts:
            times.append(sortTimer(sort,unsortedList))
            
        for place in range(len(times)):
            leader=times.index(min(times))
            if place==0:
                print '1st place:',sorts[leader].__name__,'took',times[leader],'seconds'
            elif place==1:
                print '2nd place:',sorts[leader].__name__,'took',times[leader],'seconds'
            elif place==2:
                print '3rd place:',sorts[leader].__name__,'took',times[leader],'seconds'
            else:
                print str(place+1)+'th place:',sorts[leader].__name__,'took',times[leader],'seconds'
            del times[leader]
            del sorts[leader]

def main():
    sorts=[timSort,reemSort]
    N=100000
    sortTester(sorts,N)

if __name__ == "__main__":
    main()
