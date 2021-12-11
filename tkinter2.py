from tkinter import *
import random

class MyGui:
    colors = ['red', 'green', 'blue', 'yellow', 'orange', 'pink', 'cyan', 'purple']
    fonts = ['方正舒体','方正姚体','楷体','隶书','Microsoft YaHei UI']

    def __init__(self,parent,title='popup'):
        parent.title(title)
        self.fontsize=10
        self.growing=False
        self.lab=Label(parent,text='╮(￣▽￣")╭',fg='white',bg='navy')
        self.lab.pack(expand=YES,fill=BOTH)
        Button(parent, text='spam', command=self.reply).pack(side=RIGHT)
        Button(parent, text='grow', command=self.grow).pack(side=LEFT, fill=X)
        Button(parent, text='stop', command=self.stop).pack(side=LEFT, fill=X)

    def reply(self):
        self.fontsize += 5
        color=random.choice(self.colors)
        self.lab.config(bg=color,
                        font=('courier',self.fontsize,'bold italic'))

    def grow(self):
        self.growing=True
        self.grower()


    def grower(self):
        if self.growing:
            self.fontsize += 5
            color=random.choice(self.colors)
            font= random.choice(self.fonts)
            self.lab.config(bg=color,
                            font=(font, self.fontsize, 'bold'))
            self.lab.after(250, self.grower)

    def stop(self):
        self.growing=False

class MySubGui(MyGui):
    colors = ['grey','violet']

MyGui(Tk(),'main')
MyGui(Toplevel())
# MySubGui(Toplevel())
mainloop()

