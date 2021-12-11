from abc import ABCMeta,abstractmethod

class Super():
    def method(self):
        print('in Super.method')
    def delegate(self):
        self.action()


class Inheritor(Super):
    pass

class Replacer(Super):
    def method(self):
        x=44
        print('in Replacer.method')

y=Replacer()
y1=y.method()



class Extender(Super):
    def method(self):
        Super.method(self)
        print('in Extender.method')

class Provider(Super):
    def action(self):
        print('in Provider.action')

if __name__=='__main__':
    for klass in (Inheritor,Replacer,Extender):
        print('\n'+klass.__name__)
        klass().method()
    print('\nProvider...')
    x=Provider()
    x.delegate()