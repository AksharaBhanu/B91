#accept a number from user and print its double
a=input('Plz enter a number')

if a.isnumeric():
    b=int(a)
    d=b*2
    print(d)
else:
    print('invalid input')

print('End')

#accept age from user and print if user is eligible for voting