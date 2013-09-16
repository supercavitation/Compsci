import math

def trapezoidCalculator(y1, y2, width):
    return ((y1+y2)/2)*width

equationInput=raw_input('Enter the equation with x as the variable: ')
interval1=float(raw_input('From: '))
interval2=float(raw_input('To: '))
subintervals=int(raw_input('With how many subintervals? '))
width=(interval2-interval1)/subintervals
equation=list(equationInput)
area=0
for i in range (0, subintervals):
    x1=i*width+interval1
    equation1 = map(lambda w: str.replace(w, 'x', x1), equation)
    equation1= ''.join(equation1)
    y1=eval(equation1)
    x2=(i+1)*width+interval1
    equation2 = map(lambda w: str.replace(w, 'x', x2), equation)
    equation2= ''.join(equation2)
    y2=eval(equation2)
    area=area+trapezoidCalculator(y1, y2, width)

print area
