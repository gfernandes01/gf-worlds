import sys
from tkinter import *
import time
import random

tempo = 0
def set_timer():
    global tempo
    tempo = tempo + int(e1.get())
    l1.config(text=f'SETADO {tempo}')
    return tempo

def countdown():
    global tempo
    if tempo > 0:
        print(tempo)
        l1.config(text=tempo)
        tempo -= 1
        l1.after(1000, countdown)
    elif tempo == 0:
        print('end')
        l1.config(text="FIM")

root = Tk()
root.title('Countdown')
root.geometry('200x160')
root.config(background='orange')

l1 = Label(root, font='times 20', fg='red', bg='orange')
l1.grid(row=1, column=2)
l1.config(text='CONTADOR')

times = StringVar()
e1 = Entry(root, textvariable=times)
e1.grid(row=3, column=2)

button1 = Button(root, text='SET', width=21, bd=2, fg='red', command=set_timer)
button1.grid(row=4, column=2, padx=21, pady=5)
button2 = Button(root, text='START', width=21, bd=2, fg='red', command=countdown)
button2.grid(row=6, column=2, padx=21)

root.mainloop()