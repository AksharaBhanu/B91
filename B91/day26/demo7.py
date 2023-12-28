from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print('Bow Bow')


class Cat(Animal):
    def make_sound(self):
        print('Meow Meow')


class Cow(Animal):
    def make_sound(self):
        print('Amboo')


animals=[Dog(),Cat(),Cow(),Cow(),Cat()]
for animal in animals:
    animal.make_sound()
