
def test(*a): #packing
    print(a)


test(10,20,30)


def test2(a,b,c):
    print(a,b,c)


test2(10,20,30)

list1=[10,20,30]

test2(list1[0],list1[1],list1[2])

test2(*list1) #unpacking

t1=(10,20,30)
test2(*t1)

s1={10,20,30}
test2(*s1)

d1={'k1':10,'k2':20,'k3':30}
test2(*d1.values())
test2(*d1)
test2(*d1.items())



