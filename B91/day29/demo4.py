my_function=lambda : print('hi')
my_function()

(lambda : print('hi'))()


my_function=lambda n: print(n)
my_function('Bye')

(lambda n: print(n))('Bye')

my_function=lambda x,y: x+y
print(my_function(10,20))

print((lambda x,y: x+y)(10,20))

print((lambda x,y: [x+y,x*y])(10,20))