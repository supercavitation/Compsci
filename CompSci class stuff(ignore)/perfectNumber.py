#Joshua Bloch
#2/14/13
#perfect numbers
x=1
counter=0
number=int(raw_input('Enter a number: '))
while number>x:
    if number%x==0:
        counter=counter+x
    x=x+1
if counter==number:
    print 'Perfect'
else:
    print 'Not Perfect'
    
