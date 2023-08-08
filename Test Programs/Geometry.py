
import math

class RegularPolygon:
    def __init__(self, n=3, side=1, x=0, y=0):
        self.n = n
        self.side = side
        self.x = x
        self.y = y
    
    def getPerimeter(self):
        return self.n * self.side
    
    def getArea(self):
        numerator = self.n * (self.side * self.side)
        denominator = 4 * (math.tan(math.pi/self.n))
        area = numerator / denominator
        return round(area,2)

