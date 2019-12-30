import math

class Circle:
    '''

     This circle class models a circle object.

    '''
    def __init__(self,radius = 1.0, color="red"):
        self.radius = radius
        self.color = color

    def getRadius(self):
        return self.radius
    
    def setRadius(self,radius):
        self.radius = radius

    def getArea(self):
        return self.radius**2 * math.pi

    def getColor(self):
        return self.color
    
    def setColor(self,color):
        self.color = color

    def toString(self):
        return f"Circle[radius={self.radius} color={self.color}]"


if __name__ == '__main__':
    c = Circle()
    print(c.getRadius())
    c1 = Circle(2.0)
    print(c1.getRadius())

    print(c1.toString())