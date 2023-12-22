class FD:

    def __init__(self,amount):
        self.__amount=amount  #hide the data

    def check_fd_balace(self,period): #binding this method with amount--- encapsulation
        if period>0:
            self.__amount+=(self.__amount * (period/12) * 6)/100
            print(self.__amount)
        else:
            print('invalid period')



a=FD(100)

a.check_fd_balace(12)