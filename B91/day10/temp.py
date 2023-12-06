msg='Hi {} GM,ur {} thanks-{}'
print(msg.format('Ravi','simple','bhanu'))

msg='Hi {2} GM,ur {1} thanks-{0}'
print(msg.format('Ravi','simple','bhanu'))

msg='Hi {0} GM,ur {0} thanks-{0}'
print(msg.format('Ravi'))

msg='Hi {name} GM,ur {char} thanks-{by}'
print(msg.format(name='Ravi',char='simple',by='bhanu'))

msg.replace()