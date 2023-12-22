class ATM:
    def __init__(self,init_deposit,pin):
        self.balance=init_deposit
        self.pin=pin

    def authenticate(self,pin):
        if self.pin==pin:
            print('PIN is correct')
            return True
        else:
            print('PIN is NOT correct')
            return False

    def check_balance(self,pin):
       if self.authenticate(pin):
        print('balance is',self.balance)
       else:
        print('sorry')

    def deposit(self,amount):
        if amount>0:
            self.balance=self.balance+amount
            print('Balance is',self.balance)
        else:
            print('invalid deposit')

    def withdraw(self,pin,amount):
        if self.authenticate(pin) :
            if amount >0:
                if amount<=self.balance :
                    print("Zrrrrrr: please collect the amount")
                    self.balance-=amount
                    print('Balance after withdraw:', self.balance)
                else:
                    print('insufficient balance')
            else:
                print('invalid amount')
        else:
            print('ur not authorized')


a=ATM(10000,123)
a.balance=100002
a.withdraw(123,100001)
