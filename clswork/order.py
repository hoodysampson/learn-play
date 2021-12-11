
class Lunch:

    def __init__(self):
        self.cus=Customer()
        self.eply=Employee()

    def order(self,foodName):
        self.cus.placeOrder(foodName,self.eply)

    def result(self):
        self.cus.printfood()



class Customer(Lunch):

    def __init__(self):
        self.food=''

    def placeOrder(self,foodName,employee):
        self.eply=employee
        # self.eply.takeorder(foodName)
        # self.food=foodName
        self.food=employee.takeorder(foodName)

    def printfood(self):
        print(self.food.name)
        print('%s received %s from %s'%(
            self.__class__.__name__,
            self.food.name,
            self.eply.__class__.__name__
        ))


class Employee:

    def takeorder(self,foodName):
        return Food(foodName)


class Food:

    def __init__(self, name):
        self.name=name

l=Lunch()
l.order('jiba')
l.result()
l.order('burrito')
l.result()
c=Customer()
print(c.__dict__)









