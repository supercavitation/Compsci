#Joshua Bloch
#1/30/13
#Change
change=int(raw_input ('Input a number of cents: '))
print change, ('cents is'), change/25, ('quarters,'), (change%25)/10, ('dimes,'), (((change%25)%10)/5), ('nickels'), (((change%25)%10)%5), ('pennies.')
           
