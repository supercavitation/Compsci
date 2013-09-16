#Joshua Bloch
#2/19/13
#Change with loops
quarters=0
dimes=0
nickels=0
pennies=0
cents=int(raw_input('Enter the number of cents you need to give in change: '))
while cents>=25:
    cents=cents-25
    quarters=quarters+1
print 'Quarters:', quarters
while cents>=10:
    cents=cents-10
    dimes=dimes+1
print 'Dimes:', dimes
while cents>=5:
    cents=cents-5
    nickels=nickels+1
print 'Nickels:', nickels
while cents>=1:
    cents=cents-1
    pennies=pennies+1
print 'Pennies:', pennies
