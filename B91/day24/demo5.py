class A:        #Arvinda
    def __init__(self,i):
        self.iv=i


class B(A): #Bhanu

    def __init__(self,n=None):
        super().__init__(n) #calling super class constructor from child class constructor



obj1=B()
print(obj1.iv)

obj2=B(10)
print(obj2.iv)