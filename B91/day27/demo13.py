import traceback
def f1():
    raise ValueError(0)

def f2():
    try:
        f1()
    except Exception as e:
        traceback.print_exc()
        print('in f2')

def f3():
    f2()

f3()

#exception propagation