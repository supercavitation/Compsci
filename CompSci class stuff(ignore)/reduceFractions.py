#Joshua Bloch
#3/11/13
#reduce fractions

def gcf(num1,num2):
    biggestPossibleGCF= min(num1,num2)
    while biggestPossibleGCF > 1:
        if num1%biggestPossibleGCF==0 and num2%biggestPossibleGCF==0:
            return biggestPossibleGCF
        biggestPossibleGCF-=1
            
    
numerator = int(raw_input('Enter the numerator: '))
denominator = int(raw_input('Enter the denominator: '))
gcf=gcf(numerator, denominator)
print str(numerator/gcf)+'/'+str(denominator/gcf)
