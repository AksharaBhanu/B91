#add company attribute and create 2 Emp object
class Emp:
    company='TCS'   #class variable
    def __init__(self,name):
        self.emp_name=name  #instance variable


Emp.company='TCS pvt ltd'

e1=Emp('Bhanu')
print(e1.emp_name)

print(Emp.company)
print(e1.company)

e2=Emp('Ravi')
print(e2.emp_name)
print(Emp.company)
print(e2.company)
