#Joshua Bloch
#2/4/13
#unit 2 demo of conditionals - positive, negative, zero program

number=float(raw_input('Enter a number: '))
if number<0:
    print ('Negative.')
elif number>0:
    print ('Positive.')
else:
    print ('Zero.')
if number==7:
    print ('Your number is lucky!')
elif number==13:
    print ('Your number is very unlucky!')
else:
    print ('Your number is boring.')

