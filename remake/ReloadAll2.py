import types
from importlib import reload
from hoody.ReloadAll import try_reload,tester

def transitive_reload(objects,visited):
    for obj in objects:
        if type(obj)==types.ModuleType and obj not in visited:
            print('reloading---' + obj.__name__)
            try_reload(obj)
            visited.add(obj)
            transitive_reload(obj.__dict__.values(),visited)

def reload_all(*args):
    transitive_reload(args,set())

if __name__=='__main__':
    tester(reload_all,'hoody.ReloadAll')

# reload_all(tkinter)