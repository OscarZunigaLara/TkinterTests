#https://www.tutorialspoint.com/python/python_gui_programming.htm

from tkinter import *
from tkinter import messagebox


ValidUsser= "Tandoori7"
ValidPasswd="AAA"

def printingTest():
    print("Testing 1 2 3")
    messagebox.showinfo('OwO')

def gettingUsser():
    Usser= Ent1.get()
    print(Usser)

def gettingPassword():
    Password = Ent2.get()

def CloseWindow():
    global window
    window.quit()

window = Tk()

window.title("MANAGMENT")

window.geometry('400x200')


Labl1 = Label(window , text="Introduce tu Usuario")
Labl2 = Label(window, text="Introduce Contraseña")


Ent1 = Entry(window)
Ent2 = Entry(window)

BTN1 = Button(window, text =("INICIAR SESIÓN")  , command=gettingUsser())
BTN2 = Button(window, text=("Crear Cuenta Nueva"), command=gettingPassword)
BTN3 = Button(window, text="Cerrar", commad=CloseWindow())


BTN1.grid(column=1, row=3)
BTN2.grid(column=0, row=3)
BTN3.grid(column=2, row=0)

Ent1.grid(column=1, row=0)
Ent2.grid(column=1, row=1)

Labl1.grid(column=0, row=0)
Labl2.grid(column=0, row=1)

window.mainloop()


