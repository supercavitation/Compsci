#Joshua Bloch
#1/24/13
#Slope calculator

var =1
while var ==1:
    x1=float(raw_input('x1: '))
    y1=float(raw_input('y1: '))
    x2=float(raw_input('x2: '))
    y2=float(raw_input('y2: '))

    if x1==x2:
        print 'The slope is undefined.'
        print 'The equation of the line is x=', x1
        count=int(raw_input('Press 0 to exit, or 1 to continue.'))
        if count==0:
            break
        
    else:
        slope= (y1-y2)/(x1-x2)

        print ('The slope is'), slope

        if slope==1.0: 
            if y1-(x1*slope)==0.0:
                print ('The equation of the line is y=x')
            else:
                if y1-(x1*slope)>0:
                    print ('The equation of the line is y=x+'), y1-(x1*slope)
                else:
                    print ('The equation of the line is y=x'), y1-(x1*slope)
        else:
            if slope==-1.0:
                if y1-(x1*slope)==0.0:
                    print ('The equation of the line is y=-x')
                else:
                    if y1-(x1*slope)>0:
                        print ('The equation of the line is y=-x+'), y1-(x1*slope)
                    else:
                        print ('The equation of the line is y=-x'), y1-(x1*slope)
            else:
                if y1-(x1*slope)==0.0:
                    print ('The equation of the line is y='), slope, ('x')
                else:
                    if y1-(x1*slope)>0:
                        print ('The equation of the line is y='), slope, ('x+'),  y1-(x1*slope)
                    else:
                        print ('The equation of the line is y='), slope, ('x'),  y1-(x1*slope)

    count=int(raw_input('Press 0 to exit, or 1 to continue.'))
    if count==0:
        break
