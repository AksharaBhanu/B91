#accept pin - if its wrong for 3rd time also block the card
class CardBlocked(Exception):
    def __init__(self,msg):
        super().__init__(msg)


for i in range(1,4):
   pin=int(input('plz enter the PIN'))
   if pin==123:
       print('Welcome')
       break
   elif i==3:
       raise CardBlocked('Your Card is Blocked')  #throw
   else:
       print('invalid pin ,ply try again')