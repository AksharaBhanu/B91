class A:
    def __init__(self,i):
        self.iv=i


class B(A):
    pass
            #default constructor




obj=B(100)
print(obj.iv)