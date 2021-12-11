#https://zhuanlan.zhihu.com/p/98440398


class Mymeta(type):
    def __init__(self,name,bases,dic):
        super().__init__(name,bases,dic)
        print('===>MyMeta.__init__')
        print(self.__name__)
        print(dic)
        print(self.yaml_tag)

    def __new__(cls, *args, **kwargs):
        print('===>MyMeta.__new__')
        print(cls.__name__)
        return type.__new__(cls,*args,**kwargs)

    def __call__(self, *args, **kwargs):
        print('===>MyMeta.__call__')
        obj=self.__new__(self)
        self.__init__(self,*args,**kwargs)
        return None





class Foo(metaclass=Mymeta):
    yaml_tag='!Foo'

    def __init__(self,name):
        print('Foo.__init__')
        self.name=name

    def __new__(cls, *args, **kwargs):
        print('Foo.__new__')
        return object.__new__(cls)


f=Foo('hoody')
print('-'*80)
# m=Mymeta('oli',Mymeta.__bases__,dict(Mymeta.__dict__.items()))
# m('jiba',Mymeta.__bases__,dict(Mymeta.__dict__.items()))

# f1=Foo('oli')
