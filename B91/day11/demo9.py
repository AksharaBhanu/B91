msg='Hi {}, please join today at {}, Thanks-{}'
cmsg=msg.format('Ravi','7pm','Bhanu','India')
print(cmsg)

cmsg=msg.format('Suray','8PM','Kumar')
print(cmsg)

msg='Hi {1}, Bye {0} Thank you {1}'
cmsg=msg.format('Ravi','Bhanu')
print(cmsg)

msg='Hi {name}, thank you {name} from {city}'
cmsg=msg.format(name='Ravi',city='Agra')
print(cmsg)
