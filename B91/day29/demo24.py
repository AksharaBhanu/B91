
def m2():
    print('Bye')
def m1(m):
    print('Hi')
    m()
    return m2

def script():
    print('This is script')


script=m1(script)
script()
