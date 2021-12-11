from hoody.clswork.classtool import AttrDisplay

class Person(AttrDisplay):
    def __init__(self,name,job=None,pay=0):
        self.name=name
        self.job=job
        self.pay=pay
    def lastname(self):
        return self.name.split()[1]
    def giveraise(self,percent):
        self.pay*=(1+percent)
    def __repr__(self):
        return '[%s:%s,%s,%d]'%(self.__class__.__name__,self.name,self.job,self.pay)

class Manager(Person):
    def __init__(self,name,pay):
        Person.__init__(self,name,'manager',pay)
    def giveraise(self,percent,bonus=.10):
        Person.giveraise(self,percent+bonus)

class Department:
    def __init__(self,*args):
        self.member=list(args)
    def addMember(self,person):
        self.member.append(person)
    def giveraise(self,percent):
        for person in self.member:
            person.giveraise(percent)
    def showall(self):
        for person in self.member:
            print(person)





if __name__ == '__main__':
    bob=Person('Bob Smith')
    sue=Person('Sue Gould',job='editor',pay=2000)
    print(bob)
    print(sue)
    sue.giveraise(0.1)
    print(sue)
    tom=Manager('Tom Anderson',5000)
    tom.giveraise(0.1)
    print(tom)
    print('-'*20+'Department Brief'+'-'*20)
    dept=Department(bob,sue)
    dept.addMember(tom)
    dept.giveraise(0.1)
    dept.showall()
    print(Manager.__base__)
