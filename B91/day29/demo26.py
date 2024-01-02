
def m2():
    print('logout')

def pre_post_condition(m):
    print('login')
    m()
    return m2

@pre_post_condition           # adding additional capablity (pre_post_condition) without chaning existing function->script
def script():
    print('This is script')

script()
