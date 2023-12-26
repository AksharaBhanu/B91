class A:        #Arvinda
    def __init__(self,i):
        self.iv=i


class B(A): #Bhanu

    def __init__(self,n=None):
       print('Welcome to B class')      # we can write any valid code before calling parent class constructor
       A.__init__(self,n)           #another way of calling parent class constructor



obj1=B()
print(obj1.iv)

obj2=B(10)
print(obj2.iv)