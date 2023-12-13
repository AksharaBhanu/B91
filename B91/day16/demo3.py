#find the sum of n numbers : 4--> 1+2+3
n=int(input('plz enter a number'))
sum=0
for i in range(1,n+1):
    # sum=sum+i
    sum+=i
print(sum)