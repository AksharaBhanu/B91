def m2(temp):
    print('this is m2')
    return temp


@m2
def m1():
    print('this is m1')


m1()
