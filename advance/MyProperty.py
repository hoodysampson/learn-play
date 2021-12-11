

class MyProperty:

    def __init__(self,mget=None,mset=None,mdel=None,mdoc=''):
        self.mget=mget
        self.mset=mset
        self.mdel=mdel
        self.__doc__=mdoc

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.mget is None:
            raise AttributeError('cannot get attribute')
        return self.mget(instance)

    def __set__(self, instance, value):
        if self.mset is None:
            raise AttributeError('cannot get attribute')
        self.mset(instance,value)

    def __delete__(self, instance):
        if self.mdel is None:
            raise AttributeError('cannot get attribute')
        self.mdel(instance)



class Person:
    def __init__(self,name):
        self.name=name
    def getName(self):
        print('Get...')
        return self.name

    def setName(self,value):
        print('Set...')
        self.name=value
    def delName(self):
        print('Delete...')
        del self
    P= MyProperty(getName,setName,delName)



p=Person('jiba')
print(p)
print(p.P)

j=Person('lanzi')
print(j.P)
print(p.P)




