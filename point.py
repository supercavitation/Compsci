#Joshua Bloch
#5/14/13
#graph
class Point:
    def __init__(self, x,y):
        self.x=float(x)
        self.y=float(y)
    def __str__(self):
        return '['+str(self.x)+','+str(self.y)+']'
    def quadrant(self):
        if self.x==0 or self.y==0:
            return -1
        if self.x>0:
            if self.y>0:
                return 1
            else:
                return 4
        else:
            if self.y>0:
                return 2
            else:
                return 3

    def distance_to_point(self,other):
        return ((other.y-self.y)**2+(other.x-self.x)**2)**0.5

x1=float(raw_input('x1: '))
y1=float(raw_input('y1: '))
x2=float(raw_input('x2: '))
y2=float(raw_input('y2: '))
x3=float(raw_input('x3: '))
y3=float(raw_input('y3: '))
fpoint=Point(x1,y1)
spoint=Point(x2,y2)
tpoint=Point(x3,y3)

print fpoint,'is in quadrant',Point.quadrant(fpoint)
print spoint,'is in quadrant',Point.quadrant(spoint)
print tpoint,'is in quadrant',Point.quadrant(tpoint)
distance1=fpoint.distance_to_point(spoint)
distance2=fpoint.distance_to_point(tpoint)
distance3=spoint.distance_to_point(tpoint)
print 'The perimeter of the triangle is', distance1+distance2+distance3
