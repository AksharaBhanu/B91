class Father:

    def property(self):
        print('Car, House ,Site..')

    def marriage(self):
        print('Arranged Marriage')


class Son(Father):
    def marriage(self):
        print('Love Marriage')

s1=Son()
s1.property()
s1.marriage()

