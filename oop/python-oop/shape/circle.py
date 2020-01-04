import math
class Circle:
    def __init__(self,radius,color):
        self.radius = radius
        self.color = color

    def getRadius(self):
        return self.radius

    def setRadius(self,radius):
        self.radius = radius

    def getColor(self):
        return self.color
    
    def setColor(self,color):
        self.color = color

    def getArea(self):
        return self.radius**2 *math.pi

class Cylinder(Circle):
    def __init__(self, radius, color,height):
        super().__init__(radius, color)
        self.height = height

    def getHeight(self):
        return self.height

    def setHeight(self,height):
        self.height = height

    def getVolume(self):
        return self.getArea() *self.height

