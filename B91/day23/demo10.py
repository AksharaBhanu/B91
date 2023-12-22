class ATM:
    def __init__(self,init_deposit,pin):
        self.__balance=init_deposit
        self.__pin=pin

    def __authenticate(self,pin):
        if self.__pin==pin:
            print('PIN is correct')
            return True
        else:
            print('PIN is NOT correct')
            return False

    def check_balance(self,pin):
       if self.__authenticate(pin):
        print('balance is',self.__balance)
       else:
        print('sorry')

    def deposit(self,amount):
        if amount>0:
            self.__balance=self.__balance+amount
            print('Balance is',self.__balance)
        else:
            print('invalid deposit')

    def withdraw(self,pin,amount):
        if self.__authenticate(pin) :
            if amount >0:
                if amount<=self.__balance :
                    print("Zrrrrrr: please collect the amount")
                    self.__balance-=amount
                    print('Balance after withdraw:', self.__balance)
                else:
                    print('insufficient balance')
            else:
                print('invalid amount')
        else:
            print('ur not authorized')


a=ATM(10000,123)
a.check_balance(123)
a.deposit(100)
a.withdraw(123,10001)
