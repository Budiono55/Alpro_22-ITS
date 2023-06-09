# Zaki Zaidan Akbar
# 5007221058

import math

class Circle:
    #construct a circle object
    def __init__(self, radius=1):
        self.radius = radius
    
    def getPerimeter(self):
        return 2 * math.pi * self.radius
    
    def getArea(self):
        return math.pi * self.radius ** 2
    
    def setRadius(self, radius):
        self.radius = radius

c = Circle(5)
r = c.getArea(6)
print(r)