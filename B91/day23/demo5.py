class A:
    def __init__(self):
        self.p=10     #public member---we can access from anywhere
        self.__q=20  #private member----we can access only with in the class

    def m1(self):
        print(self.p)   #with in the class we can access public memeber
        print(self.__q) #with in the class we can access private memeber

    def __m2(self):
        print(self.p)   #with in the class we can access public memeber
        print(self.__q) #with in the class we can access private memeber

    def m3(self):
        self.__m2()

a=A()
print(a.p)
# print(a.__q) #we cant access private memeber from outside of the class
a.m1()
a.m3()