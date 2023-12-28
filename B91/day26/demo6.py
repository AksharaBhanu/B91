from abc import ABC,abstractmethod

class A(ABC):
    cv=10

    def __init__(self):
        self.iv=100
    def im(self):
        print('im A')

    @classmethod
    def cm(cls):
        print('cm A')

    @staticmethod
    def sm():
        print('sm A')

    @abstractmethod
    def am(self):
        pass

class B(A):
 def am(self):
     print('am of B')


print(A.cv)
A.cm()
A.sm()

obj=B()
obj.im()
print(obj.iv)

