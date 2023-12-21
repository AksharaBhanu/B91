# create a 'Student' class with name & id as attributes
# create 2 student objects and print the respective name and id
#write the code and post it in slack
class Student:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def print_student_info(self):
        print('Name:', self.name)
        print('id:',self.id)

s1=Student('Akash','a1')
s2=Student('Bhuumi','a2')

print(s1.name)
s1.print_student_info()

s2.print_student_info()