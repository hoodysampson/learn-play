import sys

class MyList:

    def __init__(self, inst) -> iter:
        self._var = [i for i in inst]

    def __repr__(self):
        return '%s' % self._var

    def __iter__(self):
        return (i for i in self._var)

    def append(self, other):
        self._var += [other]
        return self._var

    def __add__(self, other):
        return self._var + [i for i in other]

    def __mul__(self, other):
        return MyList(self._var*other)

    def __getitem__(self, item):
        return self._var[item]

    def pop(self, index):
        pop = self._var[index]
        self._var = self._var[:index] + self._var[index + 1:]
        return pop

    def indx(self, ele):
        index = 0
        for i in self:
            if ele == i:
                return index
            else:
                index += 1

    def __getattr__(self, item):
        return getattr(self._var,item)


    def sort(self, _new=[]):
        #cannot work with "self" but "self._var???"
        if not self._var:
            return _new
        else:
            res = self[0]
            for i in self[1:]:
                if res > i:
                    res = i
            x = self.pop(self.indx(res))
            _new.append(x)
            return MyList.sort(self)



class MyListSub(MyList):
    count=0

    def __init__(self,inst):
        MyListSub.count+=1
        MyList.__init__(self,inst)
        # print('instance was made %d time(s)'%MyListSub.count)

    @staticmethod
    def NumOfInst():
        print('instance was made %d time(s)'%MyListSub.count)


    def __add__(self, other):
        self.count+=1
        return '%s method called %d times->%s'%(self.__add__,self.count,MyList.__add__(self,other))


if __name__=='__main__':
    x = MyList((1, 2, 3))
    y = MyList('haha')
    print(y*3)
    for i in range(5): x.append(i)
    print(x[:-3])
    print(x.pop(3))
    print(x.indx(4))
    print(x.sort())
    z=MyListSub((1,2,3))
    z1=MyListSub((4,5,6))
    print(z+[1,2,3])
    print(z+[3,4,5])
    print(z[2])
    MyListSub.NumOfInst()
