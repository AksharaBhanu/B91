class A:
    p=10
    def __init__(self):
        self.q=20

    def m1(self):
        print(self.q)


    @classmethod
    def m2(cls):
        print(cls.p)

    def m3(self):
        print(self.q)
        print(self.p)


obj=A()

obj.m1()
A.m2()
obj.m3()
