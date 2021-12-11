
traceMe=False
def trace(*args):
    if traceMe: print('['+' '.join(map(str,args))+']')



class BuiltMixin:
    class Properties:
        def __init__(self,attrs):
            self.attrs=attrs
        def __get__(self, instance, owner):
            return getattr(instance._onInstance__wrapped.label,self.attrs)
        #Cannot directly passed "__wrapped" insttance as Client class has multiple
        #args needs to be explicitly delineated.

    builtin=['add','str','getitem']
    for i in builtin:
        exec('__%s__=Properties("__%s__")'%(i,i))

def AcsCtrl(failif):
    def onDecorator(aClass):
        class onInstance(BuiltMixin):
            def __init__(self,*args,**kwargs):
                self.__wrapped=aClass(*args,**kwargs)

            def __getattr__(self, item):
                trace('get:',item)
                if failif(item):
                    raise TypeError('private attribute fetch: ' + item)
                else:
                    return getattr(self.__wrapped, item)

            def __setattr__(self, key, value):
                trace('set:',key,value)
                if key=='_onInstance__wrapped':
                    self.__dict__[key]=value
                elif failif(key):
                    raise TypeError('private attribute change'+key)
                else:
                    setattr(self.__wrapped,key,value)

            def getattr(self,item):
                trace('__getattribute__',item)
                if item in BuiltMixin.builtin:
                    raise AttributeError('get not allowed')
                else:
                    return object.__getattribute__(self,item)

            def setattr(self,key,value):
                trace('__setattr__',key,'=>',value)
                if key in BuiltMixin.builtin:
                    raise AttributeError('set not allowed')
                else:
                    return object.__setattr__(self,key,value)

            aClass.__getattribute__=getattr
            aClass.__setattr__=setattr

        return onInstance
    return onDecorator

def Private(*attrs):
    return AcsCtrl(failif=lambda attr:attr in attrs)

def Public(*attrs):
    return AcsCtrl(failif=lambda attr:attr not in attrs)



traceMe=True

@Private('data', 'size')
class Doubler:
    def __init__(self,label,start):
        self.label=label
        self.data=start
    def size(self):
        return len(self.data)
    def double(self):
        for i in range(self.size()):
            self.data[i]=self.data[i]*2
    def display(self):
        print('%s => %s'%(self.label,self.data))



X=Doubler('X is',[1,2,3])
Y=Doubler('Y is',[-10,-20,-30])

print(X.__class__)
print(X+'hoody')
print(X[2])
X.display()
print(X)

print(Y,Y.label)
Y.jiba='spam'



