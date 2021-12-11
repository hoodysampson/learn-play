

def lessthan(x,y):return x>y
def grtrthan(x,y):return x<y

def minmax(test,seqs):
    res=seqs[0]
    for i in seqs[1:]:
        if test(res,i):
            res=i
    return res


def mymin(mylist):
    if len(mylist)>1:
        for i in mylist:
            for j in range(len(mylist)):
                try:
                    if i < mylist[j]:

                        mylist.pop(j)
                except:
                    pass

        return mymin(mylist)
    else:
        return mylist[0]

print(mymin([3,2,5,2,9,10,1,15,20]))


if __name__=='__main__':
    print('run func test',minmax(lessthan,[3,1,5,2,9]))
    print('run func test',minmax(grtrthan,[3,1,5,2,9]))