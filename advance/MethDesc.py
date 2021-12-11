

class Tracer1:

    def __init__(self,func):
        self.meth=func
        self.count=0
    def __get__(self, instance,owner):
        def wrapped(*args):
            self.count+=1
            print('%s is called %d' % (self.meth.__name__, self.count))
            self.meth(instance,*args)
        return wrapped

class Tracer2:
    def __init__(self,func):
        self.func=func
        self.count=0
    def __call__(self, *args):
        self.count+=1
        print('%s is called %d'%(self.func.__name__,self.count))
        self.func(*args)
    def __get__(self, instance, owner):
        # def wrapped(*args):
        #     return self(instance,*args)
        return lambda *arg:self(instance,*arg)


class Tracer3:
    def __init__(self,func):
        self.func=func
        self.count=0
    def __call__(self, *args, **kwargs):
        self.count+=1
        print('%s is called %d' % (self.func.__name__, self.count))
        self.func(*args)
    def __get__(self, instance, owner):
        return wrapper(self,instance)


class wrapper:
    def __init__(self,desc,subj):
        self.desc=desc
        self.subj=subj
    def __call__(self, *args, **kwargs):
        return self.desc(self.subj,*args,**kwargs)

def tracer(func):
    def wrapped(*args):
        wrapped.count+=1
        print('%s is called %d' % (func.__name__, wrapped.count))
        return func(*args)
    wrapped.count=0
    return wrapped



class Person:

    def __init__(self,name,pay):
        self.name=name
        self.pay=pay

    @Tracer2
    def giveRaise(self,pct):
        print('Get...')
        self.pay*=(1+pct)




p=Person('bob',2000)
print(p)
p.giveRaise(0.5)
print(p.pay)