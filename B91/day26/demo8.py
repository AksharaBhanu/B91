from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def find_area(self):
        pass

class Circle(Shape):
    def find_area(self,r):
        print(3.14*r*r)

class Rectangle(Shape):
    def find_area(self, l,b):
        print(l * b)
class Triangle(Shape):
    def find_area(self, b, h):
        print(0.5 * b * h)

c1=Circle()
c1.find_area(10)

r=Rectangle()
r.find_area(10,20)

t=Triangle()
t.find_area(10,20)