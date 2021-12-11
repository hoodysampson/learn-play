
class Formula:
    'name descriptor docs'
    def __init__(self,value):
        self._var=value


    def __get__(self, instance, owner):
        print('Fetch from',owner.__name__)
        return self._var**2

    def __set__(self, instance, value):
        print('Change')
        self._var=value

    def __delete__(self, instance):
        print('Delete')
        del self._var

class Calcu:
    'by setting a var attached to the client class, you actually ' \
    'put the descriptor class\'s instance inside of instance of '\
    'client class, does not make any sense though, as descriptor '\
    'works only on Class.attr level rather than Instance.attr level.'

    cons=9

    out=Formula(2)

    def __init__(self,num):
        self.value=Formula(num)

d=Calcu(3)
print(d.out)
print(Calcu.out)
d.out=4
d.value._var=5
print(d.out)
print(d.value)
print([i for i in dir(d) if not i.startswith('__')])
print(d.__doc__)

