from stream import Processor

class Upper(Processor):
    def converter(self,data):
        return data.upper()




if __name__=='__main__':
    import sys
    t1=open(r'C:\Users\Surface\AppData\Local\Programs\Python\Python38\mylife.txt')
    x=Upper(t1,
            open(r'C:\Users\Surface\AppData\Local\Programs\Python\Python38\myfile.txt','w'))
    #Don't try to overwrite an original file with open() method which first flushes all bytes out
    #of the file,always point to an empty file should you store the processed data from original file..
    x.process()

