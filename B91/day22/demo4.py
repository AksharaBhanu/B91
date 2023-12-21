#i should be able to create Emp object with only name & id or with name,id & city
class Emp:
    def __init__(self,name='Bhanu',id='A1',city=None):
        self.emp_name=name
        self.emp_id=id
        self.city=city

e0=Emp()
e1=Emp('Surya','S1')
e2=Emp('Rashmi','R1','Agra')


