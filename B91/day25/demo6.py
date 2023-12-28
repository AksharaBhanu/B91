class Training:

    def enroll(self):
        print('Visit , ask,.. fill form ,pay money')

    def attendclass(self):
        print('get up 2hrs, ready,travle,sit in the class,sleep')

    def interview(self):
        print('goto institue,wait,Mock interview, walkin interview')
class Online(Training):

    def enroll(self):
        print('Call ,ask, fill google form, payTM karo')

    def attendclass(self):
        print('get up 2sec, click join')

    def interview(self):
        print('Book slot,join,attend interview, Virtual interview')


s1=Training()
s1.enroll()
s1.attendclass()
s1.interview()

s2=Online()
s2.enroll()
s2.attendclass()
s2.interview()