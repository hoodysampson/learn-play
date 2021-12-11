'''
CardHolder the superclass for children class below is where class atrribute and attributes set by instance stored;
CardHolderP is the one using Property
CardHolderD is the one using descriptor __get__ and __set__
CardHolderG is the one using __getattr__ undefined attr fetch
CardHolderGA is the one inherits CardHolderG but fetch all attributes fetch via __getattribute__

'''



class CardHolder:
    acctlen = 8
    retireage = 59.5
    corporate = 'Bytedance'

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr





class CardHolderP(CardHolder):


    @property
    def name(self):
        return CardHolderP.corporate,self._name
    @name.setter
    def name(self,value):
        value=value.lower().replace(' ','_')
        self._name=value

    def getAge(self):
        return self._age
    def setAge(self,value):
        if value<0 or value>150:
            raise ValueError('invalid age')
        else:
            self._age=value
    age=property(getAge,setAge)

    def getAcct(self):
        return self._acct[:-3]+'***'
    def setAcct(self,value):
        value=value.replace('-','')
        if len(value)!=self.acctlen:
            raise ValueError('invalid acct number')
        else:
            self._acct=value
    acct=property(getAcct,setAcct)

    def remainGet(self):
        return self.retireage-self.age
    remain=property(remainGet)


# cp=CardHolderP('790-683-22','Hoody Sampson',41,'fengzhuang')
# print(CardHolderP)
# print(cp.name,)
# print(cp.age)
# print(cp.acct)
# print(cp.remain)


class CardHolderD(CardHolder):

    class Name:
        def __get__(self, instance, owner):
            return instance._name
        def __set__(self, instance, value):
            value=value.lower().replace(' ','_')
            instance._name=value
    name=Name()

    class Age:
        def __get__(self, instance, owner):
            return instance._age
        def __set__(self, instance, value):
            if value<0 or value>150:
                raise ValueError('invalid age')
            else:
                instance._age=value
    age=Age()

    class Acct:
        def __get__(self, instance, owner):
            return instance._acct[:-3]+'***'
        def __set__(self, instance, value):
            value=value.replace('-','')
            if len(value)!=instance.acctlen:
                raise ValueError('invalid acct')
            else:
                instance._acct=value
    acct=Acct()

    class Remain:
        def __get__(self, instance, owner):
            instance._remain=owner.retireage-instance._age
            return instance._remain
        def __set__(self, instance, value):
            raise TypeError('auto calculation')
    remain=Remain()

# cd=CardHolderD('790-683-22','Hoody Sampson',41,'fengzhuang')
# print(cd.Name())
# print(cd.name)
# print(cd.age)
# print(cd.acct)
# print(cd.remain)

class CardHolderG(CardHolder):


    def __setattr__(self, key, value):
        if key=='name':
            value=value.lower().replace(' ','_')
        elif key=='age':
            if value<0 or value>150:
                raise ValueError('invalid age')
        elif key=='acct':
            key='_acct'
            value = value.replace('-', '')
            if len(value) != self.acctlen:
                raise ValueError('invalid acct')
            else:
                self._acct = value
        self.__dict__[key]=value



    def __getattr__(self, item):
        if item=='acct':
            return self._acct[:-3]+'***'
        if item=='remain':
            return self.retireage-self.age


class CardHolderGA(CardHolderG):

    def __getattribute__(self, item):
        if item in ('name','age','addr','acctlen','retireage'):
            return object.__getattribute__(self,item)
        elif item.startswith('_'):
            return object.__getattribute__(self, item)
        else:
            #raise error to deflect the undefined attr fetch to __getattr__ it inherits from superclass
            raise AttributeError('not found')










