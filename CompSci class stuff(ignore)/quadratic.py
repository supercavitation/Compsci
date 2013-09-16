#Joshua Bloch
#2/06/13
#Quadratics
import cmath
print 'ax^2+bx+c=0'
a=float(raw_input('a='))
b=float(raw_input('b='))
c=float(raw_input('c='))
x1=-b/(2*a)
x2=(cmath.sqrt((b**2)-4*a*c))/(2*a)
if x2==0:
    print 'Double Root'
    print 'x=(', x1, ')'
elif x2==x2.real:
    print 'Two Real Roots'
    print 'x=(',x1+x2, ')'
    print 'or'
    print 'x=(',x1-x2, ')'
else:
    print 'Two imaginary Roots'
    print 'x=(',x1,'+',x2, ')'
    print 'or'
    print 'x=(',x1,'-',x2, ')'
