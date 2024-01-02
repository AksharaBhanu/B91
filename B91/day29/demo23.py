#level3 coding

def pre_condition(script):
    print('open the browser')
    print('enter the url')
    print('maximize')
    return script


@pre_condition
def auto_script1():
    print('script 1 code')



auto_script1()
