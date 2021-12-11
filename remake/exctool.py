import sys,traceback

class Myerror(IndexError):pass

jiba=Myerror('not at all')

def catch(func):
    print(func)
    try:
        func()
    except Myerror as data:
        print('got it',Myerror,data)
    else:
        print('no error caught')

def safe(func,*parg,**kargs):
    try:
        func(*parg,**kargs)
    except Exception as ex:
        print(ex)
        print(sys.exc_info())
        print(traceback.print_exc())

if __name__=='__main__':
    @safe
    def oops():
        raise jiba


