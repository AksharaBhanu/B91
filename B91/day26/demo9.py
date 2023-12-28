from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def find_area(self):
        pass

class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def find_area(self):
        print(3.14*self.r* self.r)

class Rectangle(Shape):

    def __init__(self, l,b):
        self.l = l
        self.b=b
    def find_area(self):
        print(self.l * self.b)
class Triangle(Shape):

    def __init__(self, b,h):
        self.b = b
        self.h= h
    def find_area(self):
        print(0.5 * self.b * self.h)


shapes=[Circle(10),Rectangle(10,20),Triangle(20,30)]
for shape in shapes:
    shape.find_area()
