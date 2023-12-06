msg='rain rain come again'
msg2=msg.split()
print(msg2)

msg='rain rain come again'
msg2=msg.split(' come ')
print(msg2)

msg='rain rain come again'
msg2=msg.split('go')
print(msg2)

msg='a*b*c'
msg2=msg.split('*')
print(msg2)

msg='rain rain come again'
msg2=msg.split('come')
print(msg2)

msg='rain rain come again'
msg2=msg.split('a')
print(msg2)

msg='rain\nrain\ncome\nagain'
print(msg)
msg2=msg.split('\n')
print(msg2)