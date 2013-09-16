#Joshua Bloch
#2/19/13
#baseConverter
import math
conversion=''
number=int(raw_input('Enter a base-10 number: '))
base=int(raw_input('What base would you like to convert to: '))
digits=int(math.log10(number)/math.log10(base))+1
for place in range (1, digits+1):
    exponent=digits-place
    digit=int(number/(base**exponent))
    number=number-(base**exponent)*digit
    if digit<10:
        conversion=conversion+str(digit)
    elif digit==10:
        conversion=conversion+'A'
    elif digit==11:
        conversion=conversion+'B'
    elif digit==12:
        conversion=conversion+'C'
    elif digit==13:
        conversion=conversion+'D'
    elif digit==14:
        conversion=conversion+'E'
    elif digit==15:
        conversion=conversion+'F'
print number, 'in base', base, 'is', conversion
