# Hybrid inheritance
class A:
    a1=10


class B(A):
    b1=20


class C(A):
    c1=30

class D(B,C):
    d1=40


print(D.a1)
print(D.b1)
print(D.c1)
print(D.d1)