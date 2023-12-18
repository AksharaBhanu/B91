
def test(**a): #arbitrary keyword arguments --> stored as dict
    print(a)
    print(type(a))

test(i=10,j=20,k=30)
