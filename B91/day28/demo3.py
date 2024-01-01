def double(n,y):
    print(n*2)

def my_function(arg):#higher order function
    arg(3) #calling the function arg function - arg is another name for double


my_function(double)
