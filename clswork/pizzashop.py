from employee import PizzaRobot,Server
from classtool import AttrDisplay,AttrDisplayPro,AttrDisplayEx,ListTree

class Customer:
    def __init__(self,name):
        self.name=name
    def order(self,server):
        print(self.name,'orders from',server)
    def pay(self,server):
        print(self.name,'pays to',server)

class Oven:
    def bake(self):
        print('oven bakes')

class Pizzashop(ListTree):
    def __init__(self,server):
        self.server=Server(server)
        self.chef=PizzaRobot()
        self.oven=Oven()

    def order(self,name):
        customer=Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        self.server.work()
        customer.pay(self.server)

if __name__=='__main__':
    scene=Pizzashop('patrick')
    scene.order('mike')
    print('-'*30)
    scene.order('amanda')

# class test(Pizzashop):
#     pass
#
# t=test('roberto')
# t.server