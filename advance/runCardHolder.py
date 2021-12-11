import sys

def loadclass(version)->str:
    import importlib
    modulename=sys.argv[1]
    module = importlib.import_module(modulename)
    name=modulename+version
    print('[Using: %s]'%getattr(module,name))
    return getattr(module,name)

def printholder(who):
    print(who.acct,who.name,who.age,who.remain,who.addr,sep='\\')

if __name__=='__main__':

    CardHolder=loadclass(sys.argv[2])
    bob = CardHolder('1234-5678', 'Bob Smith', 40, '123 main st')
    printholder(bob)
    bob.name = 'Bob Q. Smith'
    bob.age = 50
    bob.acct = '23-45-67-89'
    printholder(bob)

    sue = CardHolder('5678-12-34', 'Sue Jones', 35, '124 main st')
    printholder(sue)
    try:
        sue.age = 200
    except:
        print('Bad age for Sue')

    try:
        sue.remain = 5
    except:
        print("Can't set sue.remain")

    try:
        sue.acct = '1234567'
    except:
        print('Bad acct for Sue')