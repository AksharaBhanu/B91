class A:

    def __init__(self):
        print('this is A')
        self.v=10

class B:
    v=20
    def __init__(self):
        print('this is B')
        self.v =20


class C(A,B):
    def __init__(self):

        B.__init__(self)
        A.__init__(self)
        print('this is C')

obj=C()
print(obj.v)
