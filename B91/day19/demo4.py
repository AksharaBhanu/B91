
def test(a,b=0,*c):
    print('a',a)
    print('b',b)
    for i in c:
        print(i)
    print('-----')


test(10)
test(10,20)
test(10,20,30,40,50,60)

def test2(*a,b):
    print(a)
    print(b)

# test2(10)
# test(10,20)
test2(10,b=20)
test2(10,20,30,b=20)
# test2(b=10,a=20)
# test2(a=(10,20,30),b=40)
# test2(10,20)

#best pracice - keep the arbitrary arguments as the last argument
#method overloading --> 2 methods having same name diff arg--not supported in python
