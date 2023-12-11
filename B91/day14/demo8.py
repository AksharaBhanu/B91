# WAP number and print the language
language=int(input('''Please enter any below given number
    1.Kannda
    2.Hindi
    3.English
    :'''))

if language==1:
    print('You have selected Kannada')
elif language==2:
    print('You have selected Hindi')
elif language==3:
    print('You have selected English')
else :
    print('You have selected wrong option')