class Dog():
    def make_sound(self):
        print('Bow Bow')

class Cat():
    def make_sound(self):
        print('Meow Meow')

class Cow():
    def make_sound(self):
        print('Amboo')

#storing unreladed object to call the common method
animals=[Dog(),Cat(),Cow(),Cow(),Cat()] #duck typing
for animal in animals:
    animal.make_sound()