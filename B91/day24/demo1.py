class A:
    i=10

class B(A):
    pass

obj=A()
print(obj.i)

obj2=B()
print(obj2.i)
