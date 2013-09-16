#Joshua Bloch
#5/14/13
#Rectangle
class Rectangle:
    def __init__(self,length, width):
        self.length=length
        self.width=width
    def __str__(self):
        return "Rectangle with length "+str(self.length)+" and width "+str(self.width)
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*self.length+2*self.width
    def diagonal(self):
        return ((self.length)**2+(self.width)**2)**0.5

length=float(raw_input('Enter width of rectangle: '))
width=float(raw_input('Enter length of rectangle: '))
rectangle=Rectangle(length, width)
print rectangle
print "Area =", Rectangle.area(rectangle)
print 'Perimeter =', Rectangle.perimeter(rectangle)
print 'Diagonal =', Rectangle.diagonal(rectangle)
