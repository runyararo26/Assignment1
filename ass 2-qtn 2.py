import math

class Circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r**2

class Rectangle:
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):
        return self.w * self.h

def total_area(shapes):
    return sum(s.area() for s in shapes)

print(total_area([Circle(2), Rectangle(3, 4), Circle(1)]))