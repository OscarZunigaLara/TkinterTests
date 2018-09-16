#https://www.tutorialspoint.com/python/python_gui_programming.htm

from tkinter import *
from tkinter import messagebox


ValidUsser= "Tandoori7"
ValidPasswd="AAA"
VP = False
VU = False


def printingTest():
    print("Testing 1 2 3")
    messagebox.showinfo('OwO')

def gettingUsser():
    Usser= Ent1.get()
    print(Usser)
    if (Usser == ValidUsser):
        print("Valid Usser")
        VU = True
    gettingPassword()
    VALIDATE()


def gettingPassword():
    Password = Ent2.get()
    print(Password)
    if (Password == ValidPasswd):
        print("Password Correct")
        VP= True

def CloseWindow():
    window.quit()

def VALIDATE():
    if (VP and VU):
        print("FELICIDADES")
    else:
        print("WRONG")



window = Tk()

window.title("MANAGMENT")

window.geometry('400x200')


Labl1 = Label(window , text="Introduce tu Usuario")
Labl2 = Label(window, text="Introduce Contraseña")


Ent1 = Entry(window)
Ent2 = Entry(window)

BTN1 = Button(window, text =("INICIAR SESIÓN"), command=gettingUsser())
BTN2 = Button(window, text=("Crear Cuenta Nueva"), command=gettingPassword())
BTN3 = Button(window, text="Cerrar", commad=CloseWindow())


BTN1.grid(column=1, row=3)
BTN2.grid(column=0, row=3)
BTN3.grid(column=2, row=0)

Ent1.grid(column=1, row=0)
Ent2.grid(column=1, row=1)

Labl1.grid(column=0, row=0)
Labl2.grid(column=0, row=1)

window.mainloop()


