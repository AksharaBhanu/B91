class A:
    def __init__(self):
        self.__i=10         #hiding the data
        self.j=20
    def get_data(self):
        return self.__i         #encapsualtion:process of hiding the data and providing necessary  access using getter/setter method

    def set_data(self,n):
        if n>0:
            self.__i=n



a=A()
print(a.j)
a.j=-50


a.set_data(-50)
print(a.get_data())