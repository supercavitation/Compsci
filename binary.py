#Joshua Bloch
#1/30/13
#binaryConverter
var =1
while var ==1:
    binaryNumber=int(raw_input('Enter an 8-digit binary number: '))
    first=binaryNumber%10
    second=binaryNumber/10%10
    third=binaryNumber/100%10
    fourth=binaryNumber/1000%10
    fifth=binaryNumber/10000%10
    sixth=binaryNumber/100000%10
    seventh=binaryNumber/1000000%10
    eighth=binaryNumber/10000000%10

    print first+second*2+third*4+fourth*8+fifth*16+sixth*32+seventh*64+eighth*128

    count=int(raw_input('Press 0 to exit, or 1 to continue. '))
    if count==0:
        break
