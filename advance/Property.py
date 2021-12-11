

class Person:

    def __init__(self,name):
        self._name=name



    # @property
    # def name(self,hint='Initiating...'):
    #     return hint


    @property
    def name(self):
        'name property'
        print('Fetch...')
        return self._name


    @name.setter
    def name(self,value):
        print('Change...')
        self.__init__(value)

    @name.deleter
    def name(self):
        print('Del...')
        del self._name

class Staff(Person):
    corp='Oracle'
    time=0

    def __init__(self,name):
        self._name=self.corp+'==>'+name+str(self.time)
        Staff.count()
        # super().__init__(self._num)

    @staticmethod
    def count():
        Staff.time+=1
        return Staff.__new__(Person).__class__




bob=Person('Bob')
print(bob.name)
# print(Person.name.__doc__)
# print(bob.name)
# bob.name='Smith'
# print(bob.name)
# del bob.name
# print(Person.name.__doc__)
cock=Staff('bob')
print(cock.name)
cock.corp='Tecent'
cock.name='sue'
print(cock.name)
jiba=Staff('Sue')
print(Staff.count())
print(jiba.name)
