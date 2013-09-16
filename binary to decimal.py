import math
finalAnswer=''
conversion=0
conversion1=0
base1=2
number1=raw_input('Enter a number in Binary:')
number2=raw_input('Enter a number in Binary to multiply it by:')
number1=list(number1)
for place in range (0, len(number1)):
    if int(number1[0])==1:
        conversion+=2**(len(number1)-1)
    del number1[0]
number2=list(number2)
for place in range (0, len(number2)):
    if int(number2[0])==1:
        conversion1+=2**(len(number2)-1)
    del number2[0]
number1=conversion1*conversion

digits=int(math.log10(number1)/math.log10(base1))+1
for place in range (1, digits+1):
    exponent=digits-place
    digit=int(number1/(base1**exponent))
    number1=number1-(base1**exponent)*digit
    finalAnswer+=str(digit)
print finalAnswer
