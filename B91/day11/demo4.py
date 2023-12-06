msg='abc abc'
print(msg.index('b',2,-1))

msg='rain rain come again'
print(msg.replace('r','R'))
print(msg)

s1='rain rain come again'
s2=s1.replace('a','A',2)
print(s1)
print(s2)

s1='rain rain come again'
s2=s1.replace('a','A',10)
print(s1)
print(s2)

s1='rain rain come again'
s2=s1.replace('a','A',-1)
print(s1)
print(s2)

s1='abc'
s2=s1.upper()
print(s1)
print(s2)