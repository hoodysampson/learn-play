from hoody.clswork import person

def rangetest(**argspack):
    def onFunc(func):
        #python -O name.py to bypass all decorators
        if not __debug__:
            return func
        else:
            code=func.__code__
            allarg=code.co_varnames#[:code.co_argcount]
            funcname=func.__name__
            def onCall(*args,**kargs):
                # expected=list(allarg)
                positionals=allarg[:len(args)] #to cut off kargs with default values
                                               # because pargs precedes kargs as stipulated
                for (argname,(low,high)) in argspack.items():
                    ermsg = '%s\'s "%s" is out of range %d~%d'
                    ermsg = ermsg % (funcname, argname, low, high)
                    if argname in kargs:
                        if kargs[argname]<low or kargs[argname]>high:
                            raise ValueError(ermsg)

                    elif argname in positionals: #to bypass the kargs with default values
                        position= positionals.index(argname)
                        if args[position]<low or args[position]>high:
                            raise ValueError(ermsg)
                    else:
                        print('argument %s is default'%(argname))

                return func(*args,**kargs)
        return onCall
    return onFunc

class Person(person.Person):
    @rangetest(percent=(0,1))
    def giveraise(self,percent=0.2):
        self.pay=self.pay*(1+percent)



p=Person('hoody','VP',17000)
p.giveraise()
print(p.pay,p)

@rangetest(YY=(1900,2020),MM=(1,12),DD=(1,31))
def birthday(YY,MM=7,DD=22):
    print('birthday=%d-%d-%d'%(YY,MM,DD))


birthday(1989)
code=birthday.__code__
print(code.co_varnames[:code.co_argcount])
