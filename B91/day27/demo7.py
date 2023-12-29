print('Welcome')
try:
   n1=int(input('plz enter a number'))
   n2=int(input('plz enter another number'))
   result=n1/n2
except ValueError as e:
    print('Please enter number only')
except ZeroDivisionError as e:
    print('Sorry cant div by zero')
else:
    print(result)

print('Thank You')