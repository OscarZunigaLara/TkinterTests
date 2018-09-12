from tkinter import *
from tkinter import messagebox


def printingTest():
    print("Testing 1 2 3")
    messagebox.showinfo('HOLA PICNHE PUTITA', 'TE PONES BIEN CACHONDA HIJA DE TY PUTA MADRE')

window = Tk()

window.title("MANAGMENT")

window.geometry('350x200')



BTN1 = Button(window, text =("TEST")  , command=printingTest)
#BTN1.pack()
BTN2 = Button(window, text =("TEST")  , command=printingTest)
#BTN2.pack()
BTN3 = Button(window, text =("TEST")  , command=printingTest)
#BTN3.pack()

BTN1.grid(column=2, row=0)
BTN2.grid(column=3, row=0)
BTN3.grid(column=4, row=0)
window.mainloop()
