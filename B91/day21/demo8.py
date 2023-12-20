class A:
 pass           #we get empty __init__ function--> default constructor


obj1=A()

class B:
    def __init__(self):     #user defined constructor
        print('inside init of B')


obj2=B() #calling the constructor to create object