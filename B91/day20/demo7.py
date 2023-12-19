#create a function which returns sum of n numbers Ex: 3--> 1+2+3
def sumof(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum

res=sumof(4)
print(res)

