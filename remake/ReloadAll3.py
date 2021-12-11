import types
from importlib import reload
from hoody.ReloadAll import try_reload,tester

def transitive_reload(objects,visited):
    while objects:
        n=objects.pop()
        print('reloading---' + n.__name__)
        try_reload(n)
        visited.add(n)
        objects.extend(i for i in n.__dict__.values() if
                       type(i) == types.ModuleType and i not in visited)


def reload_all(*args):
    transitive_reload(list(args),set())

if __name__=='__main__':
    tester(reload_all,'hoody.ReloadAll3')
