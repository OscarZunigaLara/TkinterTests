
#https://www.tutorialspoint.com/python/python_gui_programming.htm

from tkinter import *
from tkinter import messagebox


User= "Tandoori7"
Passwd="AAA"

def printingTest():
    print("Testing 1 2 3")
    messagebox.showinfo('HOLA PICNHE PUTITA', 'TE PONES BIEN CACHONDA HIJA DE TY PUTA MADRE')

window = Tk()

window.title("MANAGMENT")

window.geometry('700x400')



BTN1 = Button(window, text =("TESTING")  , command=printingTest)
#BTN1.pack()
BTN2 = Button(window, text =("TEST")  , command=printingTest)
#BTN2.pack()
BTN3 = Button(window, text =("TEST")  , command=printingTest)
#BTN3.pack()

Labl1 = Label(window , text="Hola a todos")


Ent1 = Entry(window, text="Inserta Usuario")
BTN1.grid(column=2, row=0)
BTN2.grid(column=3, row=0)
BTN3.grid(column=4, row=0)

Ent1.grid(column=5, row=0)
window.mainloop()


