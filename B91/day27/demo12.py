
def f1():
    raise ValueError(0)

def f2():
    f1()

def f3():
    f2()

f3()

#exception propagation