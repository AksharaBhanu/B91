class A:
    def __init__(self):
        self.v=10

    def print_v(self):
        print(self.v)

    def change_v(self,new_v):
        self.v=new_v
        self.print_v()

a1=A()
print(a1.v) #10
a1.change_v(100)
