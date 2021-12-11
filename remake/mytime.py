

import time,sys
import timeit



class Time:

    def __init__(self,reps1,reps2):
        self.timer=time.process_time if sys.platform[:3]=='win' else time.time
        self.reps1=reps1
        self.reps2=reps2
        self.replist=list(range(self.reps1))

    def total(self,func,*pargs,**kargs):
        start=self.timer()
        for i in self.replist:
            ret=func(*pargs,**kargs)
        elapsed=self.timer()-start
        return (elapsed,ret)

    def bestof(self,func,*pargs,**kargs):
        best=2*32
        for i in self.replist:
            start=self.timer()
            ret=func(*pargs,**kargs)
            elapsed=self.timer()-start
            if elapsed<best:best=elapsed
        return (best,ret)


    def best_of_total(self,func,*pargs,**kargs):
        return self.bestof(self.total,func,*pargs,**kargs)




class Test(Time):

    def permute(self,seqs):
        if not seqs:
            return [seqs]
        else:
            res = []
            for i in (range(len(seqs))):
                rest = seqs[:i] + seqs[i + 1:]
                for j in self.permute(rest):
                    res.append(seqs[i:i + 1] + j)
            return res

    def forLoop(self):
        res=[]
        for i in self.replist:
            res.append(i+self.reps2)
        return res

    def listComp(self):
        return [i+self.reps2 for i in self.replist]

    def mapCall(self):
        return list(map(lambda x:x+self.reps2,self.replist))

    def genExp(self):
        return list(i+self.reps2 for i in self.replist)

    def genFunc(self):
        def gen():
            for i in self.replist:
                yield i+self.reps2
        return list(gen())


class Timer:
    def __init__(self,func):
        self.func=func
        self.alltime=0
    def __call__(self, *args, **kwargs):
        start=time.time()
        result=self.func(*args)
        elapsed=time.time()-start
        self.alltime+=elapsed
        print('%s: %.5f -> %.5f'%(self.func.__name__,self.alltime,elapsed))
        return result


def timer(label=''):
    class Timer:

        def __init__(self,func):
            self.func=func
            self.alltime=0
        def __call__(self, *args, **kwargs):
            start=time.time()
            result=self.func(*args)
            elapsed=time.time()-start
            self.alltime+=elapsed
            print('%s %s %s %.5f'%(self.func.__name__,args,label,elapsed))
            return result
    return Timer

# if __name__=='__main__':
#     Time.__init__()



# for i in (listComp,mapCall,genExp,genFunc,forLoop):
#     (bestof1, (total1, result)) = best_of_total(5, 1000, i)
#     print(bestof1,result)
#
# for test in (listComp,mapCall,genExp,genFunc,forLoop):
#     (bestof1,(total1, result))=best_of_total(5,1000,test)
#     print('%-9s:%.5f=>[%s...%s]'%
#           (test.__name__,bestof1,result[0],result[-1]))







