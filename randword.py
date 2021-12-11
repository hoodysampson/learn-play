# -*- coding: gb2312 -*-
import random
from random import randint
import json


class RandWord:

    def __init__(self,rep=10):
        self.st=0
        self.sp=rep

    def param(self,head=10,end=16,step=5):
        self.head=head
        self.end=end
        self.step=step

    def gen_word(self):
        self.param()
        lst=[]
        while self.st<self.sp:
            word=''
            for i in range(random.randint(0,self.head),
                           random.randint(self.head,self.end),
                           random.randint(1,self.step)):
                word+=chr(random.randint(97,97+25))
            lst.append(word)
            self.st+=1
        return lst

    def to_json(self):
        dic={}
        for num,word in enumerate(self.gen_word()):
            dic[num+1]=word
        j=json.dumps(dic)
        return j





