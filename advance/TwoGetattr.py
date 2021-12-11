'''
The attribute access attempt can automatically
fall back on the __getattr__ from ubiqutous __getattribute__
by either explicitly rasie AttributeError in Person and Figure
or implicitly deflect it via __getattribute__ itself in Power

'''



class Person:

    def __init__(self,name):
        self._name=name

    def __getattribute__(self, item):
        'indiscriminately catch all attempt to access instance\'s attribute'
        print('__getattribute__ %s'%item)
        if 'name' in item:
            return object.__getattribute__(self,'_name')
        elif item.startswith('__'):
            return object.__getattribute__(self, item)
        else:
            raise AttributeError('cannot find attr %s'%item)

    def __getattr__(self, item):
        'fallback of above method if the attribute cannot be accessed'
        return ('__getattr__ %s'%object.__getattribute__(self,str(item)))


    def __setattr__(self, key, value):
        print('Set %s to %s'%(key,value))
        if isinstance(value,str):
            self.__dict__[key] = value
        else:
            raise TypeError('must be \'str\' object')

    def __delattr__(self, item):
        print('Delete %s from %s'%(item,self.__name__))
        if 'name' in item:
            raise Warning('no name shall be deleted, authorization required')
        else:
            del self.__dict__[item]

p=Person('andy')
print(p.personname)
p.hisnam='jason'
print(p.hisnam)
# del p.jbname



class Figure:

    def __init__(self,num):
        self._num=num

    def __getattribute__(self, item):
        print('__getattribute__ %s'%item)
        if item.startswith('_'):
            return object.__getattribute__(self, item)
        elif 'name' in item:
            return object.__getattribute__(self, item)**2
        else:
            raise AttributeError('cannot find attr %s'%item)

    def __getattr__(self, item):
        print('__getattr__ %s'%item)
        if isinstance(self._num, int):
            return self._num ** 2
        else:
            raise AttributeError('cannot find attr %s' % item)


    def __setattr__(self, key, value):
        print('Set %s to %s'%(key,value))
        if isinstance(value,int):
            self.__dict__[key] = value
        else:
            raise TypeError('must be \'int\' object')

    def __delattr__(self, item):
        print('Delete %s from %s'%(item,self.__name__))
        if 'name' in item:
            raise Warning('no name shall be deleted, authorization required')
        else:
            del self.__dict__[item]


print('-'*80)
f=Figure(5)
print(f.jiba)
f.hisname=6
print(f.hisname)



class Power:

    def __init__(self,square,cube):
        self.square=square
        self.cube=cube

    def __getattribute__(self, item):
        print('Get %s...'%item)
        if 'cube' in item:
            return object.__getattribute__(self,'cube')**3
        elif item:
            return object.__getattribute__(self, item)


    def __getattr__(self, item):
        print('%s not found, here is default...'%item)
        return object.__getattribute__(self,'square')**2

    def __setattr__(self, key, value):
        print('Set %s to %s'%(key,value*2))
        self.__dict__[key]=value*2 if isinstance(value,int) else value+'dajiba'


    # def getCube(self):
    #     print('Get Cube...')
    #     return self._cube**3
    # def setCube(self,value):
    #     print('Set Cube...')
    #     self._cube=value
    # cub=property(getCube,setCube)

print('-'*80)
p=Power(2,3)
print(p.square)
p.cube=4
print(p.cube)
print(p.jiba)



