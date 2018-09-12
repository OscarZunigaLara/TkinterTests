from tkinter import *
from tkinter import messagebox


def printingTest():
    print("Testing 1 2 3")
    messagebox.showinfo('HOLA PICNHE PUTITA', 'TE PONES BIEN CACHONDA HIJA DE TY PUTA MADRE')

window = Tk()

window.title("MANAGMENT")

window.geometry('350x200')


#//////////////////////////////////
starSession = Button(window, text= "Iniciar Sesión" , command = printingTest)
starSession.grid(column= 3, row= 4)

NuevaCuenta = 2
#//////////////////////////////////
window.mainloop()