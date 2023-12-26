#prove that private members are not inherited
#private member--> class var instance variable class method instance method static method
class A:
    __cv=10
    def __init__(self):
        self.__iv=20

    @classmethod
    def __m1(cls):
        print('this is class method')

    def __m2(self):
        print('this is instance method')

    @staticmethod
    def __m3():
        print('this is static method')

class B(A):
    pass


# print(B.__cv)
# obj=B()
# print(obj.__iv)

# B.__m1()
# obj.__m2()
# B.__m3()