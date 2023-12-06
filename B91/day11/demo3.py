msg='rain rain go away'
print(msg.index('r')) #returns the position of 1st r
# print(msg.index('x'))
print(msg.index('r',1))

#write a code to print position of 2nd a
f=msg.index('a')
s=msg.index('a',f+1)
print('position of 2nd a is',s)