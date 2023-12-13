#find the factorial of a number : 4--> 1x2x3X4
n=int(input('plz enter a number'))
fact=1
for i in range(1,n+1):
    fact*=i

print(fact)