class Bank:

    def open_account(self):
        print('Fill the form ,submit all req doc')

    def deposit(self):
        print('Fill the challan and give amount to cashier')

    def withdraw(self):
        print('Fill the cheque and give to cashier & collect amount')

    def checkbalance(self):
        print('Give passbook and get the entry...')


class ATM(Bank):
    def withdraw(self):
        print('Insert ATM Card,Enter PIN,Enter amount and collect')

    def checkbalance(self):
        print('Insert ATM Card,Enter PIN and select mini statement')


customer1=Bank()
customer1.open_account()
customer1.deposit()
customer1.withdraw()
customer1.checkbalance()

customer2=ATM()
customer2.open_account()
customer2.deposit()
customer2.withdraw()
customer2.checkbalance()