from tkinter import *
import random

fontsize = 25
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'white', 'cyan', 'purple']


def reply(text):
    print(text)
    popup = Toplevel()
    color = random.choice(colors)
    Label(popup, text='Pop up', bg='black', fg=color).pack(side=TOP, fill=EXTENDED)
    L.config(fg=color)


def timer():
    L.config(fg=random.choice(colors))
    win.after(100, timer)
# '.after' (int=time in second, func=function you would like to carry on after this one)

def grow():
    global fontsize
    fontsize += 5
    L.config(font=('arial', fontsize, 'italic'))
    win.after(250, grow)


win = Tk(screenName='jiba')
L = Label(win, text='SPAM',
          font=('Yu Gothic', fontsize, 'italic'), fg='yellow', bg='navy',
          relief=RAISED)
L.pack(side=TOP, expand=YES, fill=BOTH)
# can only pass function without returning any value from it
Button(win, text='press', command=(lambda: reply('red')), ).pack(side=BOTTOM, fill=X)
Button(win, text='timer', command=timer).pack(side=BOTTOM, fill=X)
Button(win, text='grow', command= grow).pack(side=BOTTOM, fill=X)

L.mainloop()