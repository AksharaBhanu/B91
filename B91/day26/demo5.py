from abc import ABC,abstractmethod
class Car(ABC): #Car is an Abstract class -ABC Abstract Base Class # we cant create object
    @abstractmethod
    def start(self):#method having only header --abstract method
        pass

    @abstractmethod
    def stop(self):
        pass




class MaruthiCar(Car):#concrete class-- we can create object and call the method

    def start(self):    #mehtod having both header & body -concrete method
        print('insert key, turn right, zzzzz')

    def stop(self):
        print('turn left and remove the key')

obj=MaruthiCar()
obj.start()
obj.stop()


