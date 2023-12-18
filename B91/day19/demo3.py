def add(*a): #arbitrary arguments--interanlly all the arguments are stored as tuple
    sum=0
    for i in a:
        sum+=i
    print(sum)


add(10,20,30,40)
