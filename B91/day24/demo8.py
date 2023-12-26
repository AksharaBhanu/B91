#hierarchical inheritance
class A:
    a1=10


class B(A):
    b1=20


class C(A):
    c1=30


print(A.a1)

print(B.a1)
print(B.b1)

print(C.a1)
print(C.c1)