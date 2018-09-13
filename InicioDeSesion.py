#https://www.tutorialspoint.com/python/python_gui_programming.htm

from tkinter import *
from tkinter import messagebox


ValidUsser= "Tandoori7"
Passwd="AAA"

def printingTest():
    print("Testing 1 2 3")
    messagebox.showinfo('')

def gettingUsser():
    Usser= Ent1.get()
    print(Usser)

def gettingPassword():
    Password = Ent2.get()

def CloseWindow(self):
    self.destroy()

window = Tk()

window.title("MANAGMENT")

window.geometry('400x200')



BTN1 = Button(window, text =("INICIAR SESIÓN")  , command=printingTest)
BTN2 = Button(window, text=("Crear Cuenta Nueva"), command=gettingPassword)
BTN3 = Button(window, text="Cerrar", commad=CloseWindow(window))


Labl1 = Label(window , text="Introduce tu Usuario")
Labl2 = Label(window, text="Introduce Contraseña")


Ent1 = Entry(window)
Ent2 = Entry(window)

BTN1.grid(column=1, row=3)
BTN2.grid(column=0, row=3)
BTN3.grid(column=2, row=0)

Ent1.grid(column=1, row=0)
Ent2.grid(column=1, row=1)

Labl1.grid(column=0, row=0)
Labl2.grid(column=0, row=1)

window.mainloop()


