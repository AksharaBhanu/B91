#create a function whic returns factorial of a given number
#4--> 1x2x3x4

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

res=factorial(4)
print(res)

