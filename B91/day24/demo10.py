class A:
    v=10

class B:
    v=20


class C(A,B):
    pass


class D(B,A):
    pass

print(C.v) #10
print(D.v) #20