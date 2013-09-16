#Joshua Bloch
#2/14/13 <3
#divisors
x=1
number=int(raw_input('Enter a number: '))
while number>x:
    if number%x==0:
        print x
    x=x+1
