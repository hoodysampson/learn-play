
def decorator(func):
    def proxy(name,age):
        name+='_male'
        age+=5
        return func(name,age)
    return proxy





@decorator
def person(alias,tenure):
    corp='Bytedance'
    return '%s\'s %s, worked %d'%(corp,alias,tenure)

print(person('hoody',5))





print('-'*80)

class Dec:
    def __init__(self,C):
        self.C=C
    def __call__(self, *args, **kwargs):
        self.wrapped=self.C(*args)
        return self
    def __getattr__(self, item):
        return getattr(self.C,item)
    def __get__(self, instance, owner):
        return instance

def Test(cls):
    count=0
    class nest:

        def __init__(self,*arg):
            nonlocal count
            self.count=count
            self.wrapped=cls(*arg)
        def __call__(self, *args, **kwargs):
            self.count+=1
            print('%s was called %d'%(self.wrapped.name,self.count))
    return nest

@Test
class C:
    count=0
    def __init__(self,name,num):
        self.name=name
        self.count+=num
    def test(self):
        print('Get...')
        return self.name

c=C('hoody',2)
d=C('vicko',3)
c(1,2)
d(3,4)
c(4,5)
