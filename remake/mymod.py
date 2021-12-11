import sys

def countlines(name=input('please enter the file path')):
    line=0
    with open(name,'r') as f:
        f=f.readlines()
        for i in f:line+=i.count('\n')
    return line

def countChars(name= input('please enter the file path')):
    with open(name,'r') as f:
        f=f.read()
    return len(f)

def test(name):
    if len(sys.argv)>1:name=sys.argv[1]
    print('the file has %d lines'%countlines(name))
    print('the file has %d characters'%countChars(name))

if __name__=='__main__':
    test(r'C:\Users\Surface\AppData\Local\Programs\Python\Python38\hoody\mymod.py')


