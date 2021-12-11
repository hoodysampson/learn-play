from hoody.remake.mytime import timer

def singleton1(aClass):
    instance=None
    def onCall(*args):
        nonlocal instance
        if instance is None:
            instance=aClass(*args)
        return instance
    return onCall

def singleton2(aClass) -> object:
    def onCall(*args):
        if onCall.instance is None:
            onCall.instance=aClass(*args)
        return onCall.instance
    onCall.instance=None
    return onCall

def TracerD(aClass):
    class Wrapper:
        def __init__(self,*args):
            self.fetch=0
            self.wrapped=aClass(*args)
        def __getattr__(self, item):
            self.fetch+=1
            print('%s is traced %d'%(item,self.fetch))
            return getattr(self.wrapped,item)
    return Wrapper

class TracerC:
    def __init__(self,aClass):
        self.aClass=aClass
    def __call__(self, *args, **kwargs):
        self.wrapped=self.aClass(*args)
        return self.wrapped
    def __getattr__(self, item):
        return getattr(self.wrapped,item)


@TracerC
class Person:

    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def giveRaise(self, pct):
        print('Get...')
        self.pay *= (1 + pct)

p = Person('bob', 2000)
print(p.name,p.pay)
s= Person('sue', 5000)
print(s.name,s.pay)
p.giveRaise(0.5)
print(p.name)
print('')

@TracerC
class Mylist(list):

    def display(self):
        return 'spam'*3


l=Mylist('hoody')
print(l)
l.append('jiba')
print(l)
print(l.display())
g=Mylist('oli')
print(g)
print(g.display())

