spelen=60
sepchr='-'

def listing(module, verbose=True):
    sepline=spelen*sepchr
    if verbose:
        print(sepline)
        print('name:',module.__name__,'\n','files:',module.__file__)
        print(sepline)

    count=0
    for attr in sorted(module.__dict__):
        print('%02d）%s'%(count,attr),end='')
        if attr.startswith('_'):
            print('<built-in name>')
        else:
            print(getattr(module,attr))
        count+=1

    if verbose:
        print(sepline)
        print(module.__name__,'has %d names'%count)

if __name__=='__main__':
    from . import mydir
    listing(mydir)

