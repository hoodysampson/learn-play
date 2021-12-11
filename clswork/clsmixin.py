import importlib
from mapattr import mapattr
import pprint

def tester(listerclass,sep=False):

    class Super:
        def __init__(self):
            self.data='spam'
        def ham(self):
            pass

    class Sub(Super,listerclass):
        def __init__(self):
            self.data1='eggs'
            self.data2=42
        def spam(self):
            pass

    

    instance=Sub()

    print(pprint.pformat(mapattr(instance,True)))
    print(instance)
    print('-'*80)

def testbynames(modname,classname,sept=False):
    mod=importlib.import_module(modname)
    cls=getattr(mod,classname)
    tester(cls,sept)

testbynames('pizzashop','Pizzashop',False)


