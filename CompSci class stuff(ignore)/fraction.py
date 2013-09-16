#Joshua Bloch
#5/20/13
#fractions
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator=numerator
        self.denominator=denominator
    def __str__(self, fracNumber):
        return 'Fraction',fracNumber,'=',numerator+'/'+denominator
    def simplify(self):
        for checker in range(2,self.numerator+1):
            if self.numerator%checker=0 and self.denominator%checker=0:
                self.numerator/=checker
                self.denominator/=checker
    def __add__(self,other):
        newNumerator=self.numerator*other.denominator+self.denominator*other.numerator
        newDenominator=self.denominator*other.denominator
        return str(newNumerator)+'/'+str(newDenominator)
    def __sub__(self,other):
