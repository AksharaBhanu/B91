def add(*a): #arbitrary arguments--interanlly all the arguments are stored as tuple
    print(a)
    print(type(a))
    print('-'*5)

add()
add(10)
add(10,20)
add(10,20,30)
add(10,20,30,40)
add(10,20,30,40,50)