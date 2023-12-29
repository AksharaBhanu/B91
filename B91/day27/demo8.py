print('Welcome')

try:
   n1=int(input('plz enter a number'))
   n2=int(input('plz enter another number'))
except:
    print('in except')
    print( n1 / n2)
else:
    print('in else')
    print( n1 / n2)
finally: #always executed
    print('Thank You')  #clean up code

print('The End')