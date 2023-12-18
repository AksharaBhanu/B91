def test(*a):
    print(a)


#packing
test(10,20,30)


def test(a,b,c):
    print(a,b,c)

t=(10,20,30)
test(*t) #unpcaking