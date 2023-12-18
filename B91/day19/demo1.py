def add_number(a,b=1):
    res=a+b
    print(res)


add_number(10)
add_number(b=100,a=200)
# add_number(10,20)

def add_number2(a=1,b=2):
    print('a',a)
    print('b',b)
    res=a+b
    print(res)

add_number2(10,20)
add_number2(a=10,b=20) #keyword argument
add_number2(b=10,a=20)
add_number2()
add_number2(10)
add_number2(a=10)
#call the add_number2 by passing only b
add_number2(b=20)