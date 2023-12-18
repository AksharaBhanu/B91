for i in range(1,4):
    pin=int(input('plz enter the pin'))
    if pin==123:
        print("Welcome")
        break
    elif i==3:
        print('CARD IS BLOCKED')
    else:
        print('Sorry plz try again')