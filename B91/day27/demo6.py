print('Welcome')
try:
   n1=int(input('plz enter a number'))
   n2=int(input('plz enter another number'))
   result=n1/n2
except Exception as e:
    # print(type(e)) #ValueError  #ZeroDivisionError
    print('there was an error',e)
else:
    print(result)

print('Thank You')