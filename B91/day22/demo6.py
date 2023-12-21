class Emp:
    company='TCS'   #class variable

    def __init__(self,name):
        self.emp_name=name  #instance variable

    def print_name(self):           #instance method
        print(self.emp_name)
        print(self.company)


    @classmethod
    def print_company(cls):         #class method
        print(cls.company)


e1=Emp('Bhanu')
e1.print_name()
Emp.print_company()

e2=Emp('Ravi')
e2.print_name()
e2.print_company()