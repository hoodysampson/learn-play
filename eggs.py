# X=99
# from . import spam
# print(spam)

d1=dict(zip([i for i in range(4)],'spam'))
d2={k:v for (k,v) in zip([i for i in range(4,8)],'jiba')}
d3={k:sorted(v for v in range(4))for k in 'spam'}
print(d1,d2,d3)





