class A:

    def testA(self):
        print('test of A')

    def checkA(self):
        print('check A')

class B(A):
    def checkA(self):           #method overriding
        print('check B')


obj1=A()
obj1.testA()
obj1.checkA()

obj2=B()
obj2.testA()
obj2.checkA()