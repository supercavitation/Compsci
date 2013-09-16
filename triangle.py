#Joshua Bloch
#3/07/13
#triangle

def sideCalculator(x1,y1,x2,y2):
    return (((x1-x2)**2)+((y1-y2)**2))**0.5
    

x1=float(raw_input('x1= '))
y1=float(raw_input('y1= '))
x2=float(raw_input('x2= '))
y2=float(raw_input('y2= '))
x3=float(raw_input('x3= '))
y3=float(raw_input('y3= '))

a=sideCalculator(x1,y1,x2,y2)
b=sideCalculator(x1,y1,x3,y3)
c=sideCalculator(x2,y2,x3,y3)

s=((0.5)*(a+b+c))

area=(s*(s-a)*(s-b)*(s-c))**0.5

print 'Area='+str(area)
