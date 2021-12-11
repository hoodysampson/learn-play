class Employee:
    def __init__(self,name,salary=0):
        self.name=name
        self.salary=salary
    def giveRaise(self,pcnt):
        self.salary=self.salary*(1+pcnt)
    def work(self):
        print(self.name,'dose stuff')
    def __repr__(self):
        return '<Employee--name:%s--salary:%.2f>'% (self.name,self.salary)

class Chef(Employee):
    def __init__(self,name):
        Employee.__init__(self,name,5000)
    def work(self):
        print(self.name,'cook food')

class Server(Employee):
    def __init__(self,name):
        Employee.__init__(self, name, 3000)
    def work(self):
        print(self.name,'serve food')

class PizzaRobot(Chef):
    def __init__(self):
        Chef.__init__(self,name='robot')
    def work(self):
        print(self.name,'cook pizza')

bob=Chef('bob')
print(bob)
bob.giveRaise(-0.9)
print(bob.work())
sue=Server('sue')
print(sue)

class TwoJobs(Chef,Server):pass

tom=TwoJobs('Tom')
print(tom)

# for i in Employee,Chef,Server,PizzaRobot:
#     obj=i(i.__name__) if i != PizzaRobot else i()
#     obj.work()