#create emp class with emp_id and emp_name with 1 getter and 1 setter method

class Emp:
    def __init__(self,name,id):
        self.emp_name=name
        self.emp_id=id

    def get_emp_details(self):
        data={'name':self.emp_name,'id':self.emp_id}
        return data

    def set_emp_details(self,name,id):
        self.emp_name=name
        self.emp_id=id


e1=Emp('Asha','A1')  #calling the constructor --> create object of Emp
print(e1.get_emp_details())
e1.set_emp_details('ASHA','a1')
print(e1.get_emp_details())
