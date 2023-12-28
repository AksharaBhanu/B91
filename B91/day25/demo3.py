class A:
    def testA(self):
        print('test of A')

class B(A):
    def testA(self,v=None):
        print('test of B with',v)



obj=B()
obj.testA()
obj.testA(10)