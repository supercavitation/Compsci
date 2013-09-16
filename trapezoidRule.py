import math

def trapezoidCalculator(y1, y2, width):
    return ((y1+y2)/2)*width

def leftHandSumCalculator(y1, width):
    return y1*width

def midpointSumCalculator(y1, width):
    return y1*width

def rightHandSumCalculator(y2, width):
    return y2*width

equationInput=raw_input('Enter the equation with x as the variable: ')
interval1=float(raw_input('From: '))
interval2=float(raw_input('To: '))
subintervals=int(raw_input('With how many subintervals? '))
sumType=int(raw_input('''1) Trapezoid rule
2) Left-hand Riemann Sum
3) Midpoint Riemann Sum
4) Right-hand Riemann Sum
Choose an option: '''))
width=(interval2-interval1)/subintervals
equation=list(equationInput)
area=0
for i in range (0, subintervals):
    x1=i*width+interval1
    x2=(i+1)*width+interval1
    if sumType==1:
        equation1 = [w.replace('x',str(x1)) for w in equation]
        equation1= ''.join(equation1)
        y1=eval(equation1)
        equation2 = [w.replace('x',str(x2)) for w in equation]
        equation2= ''.join(equation2)
        y2=eval(equation2)
        area=area+trapezoidCalculator(y1, y2, width)
    elif sumType==2:
        equation1 = [w.replace('x',str(x1)) for w in equation]
        equation1= ''.join(equation1)
        y1=eval(equation1)
        area=area+leftHandSumCalculator(y1,width)
    elif sumType==3:
        x=(x1+x2)/2
        equation1 = [w.replace('x',str(x)) for w in equation]
        equation1= ''.join(equation1)
        y1=eval(equation1)
        area=area+midpointSumCalculator(y1, width)
    elif sumType==4:
        equation2 = [w.replace('x',str(x2)) for w in equation]
        equation2= ''.join(equation2)
        y2=eval(equation2)
        area=area+rightHandSumCalculator(y2, width)
    else:
        print "Not an option."

print area
