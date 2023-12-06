#replace all space with -
msg='05 Dec 2023 Tue 8PM'
msg2=msg.replace(' ','-')
print(msg2)

#replace all space with - without using replace function
msg2=msg.split()
msg3='-'.join(msg2)
print(msg3)