def my_info(name,ph,sub):
    print('name',name)
    print('ph', ph)
    print('sub', sub)
    print('-----')


my_info('Bhanu',1234,'python')

def my_info(**info):
    for key in info:
        print(key,info[key])

my_info(name='Bhanu',ph=1234,sub='python')

my_info(name='Bhanu',email='abc@gmail.com',sub='python')