class A:
    cv=10

    def __init__(self):
        self.iv=20

    @classmethod
    def m1(cls):
        print('this is class method')

    def m2(self):
        print('this is instance method')

    @staticmethod
    def m3():
        print('this is static method')


class B(A):
    pass

# print(A.cv)
# obj1=A()
# print(obj1.iv)
# A.m1()
# obj1.m2()
# A.m3()

print(B.cv)
obj2=B()
print(obj2.iv)
B.m1()
obj2.m2()
B.m3()