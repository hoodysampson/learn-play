import pprint

class MapAttr:

    def __init__(self,inst,label='',withobject=False,bysource=False):
        self.inst=inst
        print(label+pprint.pformat(self.mapattrs(withobject,bysource))+'\n')

    def filterdictvals(self,D,V):
        return {K:V2 for (K,V2) in D.items() if V2!=V}

    def invertdict(self,D):
        return {V:sorted(K for K in D.keys() if D[K]==V) for V in set(D.values())}

    # def dflr(self,cls):
    #     here=[cls]
    #     for sup in self.cls.__bases__:
    #         here+=dflr(sup)
    #     return here

    def inheritance(self):
        # if hasattr(self.inst.__class__,'__mro__'):
        return (self.inst,)+self.inst.__class__.__mro__
        # else:
        #     return [self.inst]+dflr(self.inst.__class__)

    def mapattrs(self,withobject=False,bysource=False):
        attr2obj={}
        inherits=self.inheritance()
        for attr in dir(self.inst):
            for obj in inherits:
                if hasattr(obj,'__dict__') and attr in obj.__dict__:
                    attr2obj[attr]=obj
                    break

        if not withobject:
            attr2obj=self.filterdictvals(attr2obj,object)
        return attr2obj if not bysource else self.invertdict(attr2obj)


def mapattr(inst,inverse=False):
    attr2obj={}
    for attr in dir(inst):
        for cls in inst.__class__.__mro__:
            if attr in cls.__dict__ and cls!=object:
                attr2obj[attr]=cls
                break
    if inverse is True:
        return {v:sorted(k for k in attr2obj.keys() if attr2obj[k]==v)
                for v in set(wattr2obj.values())}
    else:
        return attr2obj



class A:attr1 = 1;__slots__ = ['a','b']
class B(A): attr2 = 2;__slots__ = ['c','b'];
class C(A): attr1 = 3
class D(B, C): pass
I = D()

ma=MapAttr(I,'ATTR\n',True,True)
print(pprint.pformat(mapattr(I,True)))

