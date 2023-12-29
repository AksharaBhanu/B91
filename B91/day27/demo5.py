#accept 2 numbers from user and print div of it
print('Welcome')
n1=0
n2=0
try:
   n1=int(input('plz enter a number'))
   n2=int(input('plz enter another number'))
except:
    print('bye') #recovery code
else:
    print(n1/n2)

print('Thank You')