#https://www.tutorialspoint.com/python/python_gui_programming.htm

from tkinter import *
from tkinter import messagebox


ValidUsser= "Tandoori7"
Passwd="AAA"

def printingTest():
    print("Testing 1 2 3")
    messagebox.showinfo('HOLA PICNHE PUTITA', 'TE PONES BIEN CACHONDA HIJA DE TY PUTA MADRE')

def gettingUsser():
    Usser= Ent1.get()
    print(Usser)

def gettingPassword():
    Password = Ent2.get()

window = Tk()

window.title("MANAGMENT")

window.geometry('400x200')



BTN1 = Button(window, text =("TESTING")  , command=printingTest)
BTN2 = Button(window, text=("ENTER"), command=gettingPassword)
#BTN1.pack()


Labl1 = Label(window , text="Introduce tu Usuario")
Labl2 = Label(window, text="Introduce Contraseña")


Ent1 = Entry(window)
Ent2 = Entry(window)

BTN1.grid(column=2, row=1)
#BTN2.grid(column=2, row=1)

Ent1.grid(column=1, row=0)
Ent2.grid(column=1, row=1)

Labl1.grid(column=0, row=0)
Labl2.grid(column=0, row=1)

window.mainloop()


