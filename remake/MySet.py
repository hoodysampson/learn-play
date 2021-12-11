class Myset:

    def __init__(self,iter=[])->iter:
        self.concat(iter)


    def __repr__(self):
        return str(self._T)

    def __contains__(self, item):
        return True if item in self._T else False


    def intersec(self,other)->set:
        isc=[]
        for i in self:
            if i in other:
                isc.append(i)
        return Myset(isc)

    def union(self,other)->set:
        isc=[i for i in self]
        for i in other:
            if i not in self:
                isc.append(i)
        return Myset(isc)

    def concat(self,other):
        self._T=set()
        for i in other:
            self._T.add(i)
        return self._T


    def __or__(self, other):
        return self.intersec(other)
    def __and__(self, other):
        return self.union(other)
    def __iter__(self):
        return (i for i in self._T)
    def __len__(self):
        len=0
        for i in self:
            len+=1
        return len



class MySetSub(Myset):

    def __init__(self, *args):
        self._t = []
        for i in args:
            t=super().concat(i)
            self._t.append(t)


    def __repr__(self):
        return str(self._t)



    def intersec(self) ->set:
        copy=self._t[:]
        #this is important since "slice" can skew
        #the value of self._t since it is mutable
        t1=set()
        for i in copy[1:]:
            res=Myset.intersec(copy[0],i)
            if len(res)==0:
                t1=None
                break
            else:
                t1.update(res)
                copy[0]=t1
        return t1

    def union(self) ->set:
        copy=self._t[:]
        t1=set()
        for i in copy[1:]:
            res=Myset.union(copy[0],i)
            if len(res)==0:
                t1=None
                break
            else:
                t1.update(res)
                copy[0]=t1
        return t1


s1=Myset([1])
print(s1)
s2=Myset((9,4))
print(type(s1|s2))
print(s1&s2)
print(2 in s2)
s3=Myset('spam')
s4=Myset('spot')
print(s3|s4)
s5=MySetSub('spam','hoopy','looper','oppo','jiba')
print(s5.intersec())
print(s5.union())