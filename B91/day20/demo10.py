#a function which calls itself is called as recursive function
#if not written properly it goes to infite loop and end up with error
def test():
    print('this is test')
    test()


test()