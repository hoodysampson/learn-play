import pprint

class AttrDisplay:
    """
    Provides an inheritable display overload method that shows
    instances with their class names and a name=value pair for
    each attribute stored on the instance itself (but not attrs
    inherited from its classes). Can be mixed into any class,
    and will work on any instance.
    """

    def gatherAttr(self):
        return ''.join('\t%s=%s\n'%(attr,self.__dict__[attr])
                       for attr in sorted(self.__dict__))
        # attrs=[]
        # for key in sorted(self.__dict__):
        #     attrs+='\t%s=%s\n'%(key,getattr(self,key))
        # return ','.join(attrs)

    def __str__(self):
        return '<Instance of %s, address %s:\n%s>'%(
            self.__class__.__name__,
            id(self),
            self.gatherAttr())

class AttrDisplayPro(AttrDisplay):

    def gatherAttr(self,inst,indent=' '*4):
        #if you would save off "inst" as an argument, then the method can only
        #work for instantiated object which accessed it, instead of being a generic
        #method that process args passed into it.
        unders='Unders%s\n%s%%s\n'%('-'*77,indent)
        others='\nOthers%s\n'%('-'*77)
        privacy=[]
        result=''
        for attr in dir(inst):
            if attr[:2]=='__' and attr[-2:]=='__':
                privacy.append(attr)
            else:
                display=str(getattr(inst,attr))[:82-len(indent)-len(attr)]
                result += '%s%s=%s\n'%(indent,attr,display)
        return unders%','.join(privacy)+others+result

class AttrDisplayEx(AttrDisplay):

    def gatherAttr(self):
        return ''.join('\t%s=%s\n'%(attr,getattr(self,attr))
                       for attr in dir(self))


class ListTree(AttrDisplayPro):

    def listclass(self,aClass,indent=4):
        dots='.'*indent
        if aClass in self.__visited:
            return '\n%s<Class %s:,address%s: (see above)>\n'%(
                dots,
                aClass.__name__,
                id(aClass)
            )
        else:
            self.__visited[aClass]=True
            here = self.gatherAttr(aClass)
            above = ''
            for super in aClass.__bases__:
                above+=self.listclass(super,indent+4)
            return '\n{0}<Class {1},address {2},\n{3}{4}{5}>\n'.format(
                dots,
                aClass.__name__,
                id(aClass),
                here,above,dots
                )

    def __str__(self):
        self.__visited={}
        here = self.gatherAttr(self)
        #very tricky. if you did not pass an arg to gatherAttr(), then it works only
        #as a display method for the instance which accessed it by '.'.
        above = self.listclass(self.__class__)
        return '<Instance of {0}({1}), address {2}:\n{3}{4}'.format(
            self.__class__.__name__,
            ','.join([i.__name__ for i in self.__visited]),
            id(self),
            here,above
        )



class MapAttr:

    def __init__(self,inst,inverse=False):
        print(pprint.pformat(self.mapattr(inst,inverse)))


    def mapattr(self,inst,inverse):
        attr2obj={}
        for attr in dir(inst):
        #dont use inst.__dict__ should the __slots__ be used in case
            for cls in inst.__class__.__mro__:
                if attr in cls.__dict__ and cls!=object:
                    attr2obj[attr]=cls
                    break
        if inverse is True:
            return {v:sorted(k for k in attr2obj.keys() if attr2obj[k]==v)
                    for v in set(attr2obj.values())}
        else:
            return attr2obj



if __name__=='__main__':

    class TopTest(ListTree):
        count=0
        def __init__(self):
            self.attr1=TopTest.count
            self.attr2=TopTest.count+1
            TopTest.count+=2

    print(TopTest.count)

    class SubTest(TopTest):
        pass

    print(SubTest.count)

    X,Y=TopTest(),SubTest()
    print(Y)



