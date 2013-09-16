#Joshua Bloch
#1/24/13
#Slope calculator

x1=float(raw_input('x1: '))
y1=float(raw_input('y1: '))
x2=float(raw_input('x2: '))
y2=float(raw_input('y2: '))


if x1==x2:
    print 'The slope is undefined.'
    print 'The equation of the line is X=', x1
else:
    slope= (y1-y2)/(x1-x2)
    print ('The slope is'), slope

    print ('The equation of the line is '), slope, ('X+'),  y1-(x1*slope)
