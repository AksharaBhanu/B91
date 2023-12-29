print('Welcome')

try:
   n1=int(input('plz enter a number'))
   n2=int(input('plz enter another number'))
except:
    print('in except')
    try:
      print( n1 + n2)
    except:
      print('Cant add also')
    finally:
        print('finally1')
else:
    print('in else')
    print( n1 / n2)
finally: #always executed
     print('finally2')  #clean up code


print('The End')