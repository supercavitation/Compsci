def carrying(final,base,place,number1):
    if final>=base:
        final-=base
        number1[place-1]+=1
        final=number1[place-1]
        carrying(final,base,place-1,number1)
    return number1
    
    
number1=raw_input('Input a number to be multiplied by 11: ')
base=int(raw_input('In what base? '))
number1=list(number1)
result=[]
result.append(number1[0])
for place in range(0, len(number1)-1):
    x=len(number1)-place
    final=int(number1[place])+int(number1[place+1])
    place1=place
    while x!=0:
        if final>=base:
            final-=base
            number1[place1-1]+=1
            final=number1[place1-1]
            place1-=1
            x-=1
result.append(number1[-1])
print result
