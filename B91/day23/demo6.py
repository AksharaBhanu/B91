class A:
    c1=10   #public class variable
    __c2=20 #private class variable

    @classmethod
    def m1(cls):
        print(cls.c1)
        print(cls.__c2)

    @classmethod
    def __m2(cls):
        print(cls.c1)
        print(cls.__c2)

    @classmethod
    def m3(cls):
        cls.__m2()


print(A.c1)
A.m1()
#A.m2() outside the class we cant access private class method
A.m3()
print(A.__c2) #outside the class we cant access private class variable