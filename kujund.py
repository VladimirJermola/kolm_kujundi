import os
from tkinter import *
from tkinter.messagebox import showinfo


def silider():
    os.system("python app.py")

def rectangle():
    os.system("python app2.py")

def stadium():
    os.system("python app3.py")

window = Tk()
window.title("Vali kujund")
#window.geometry("500x500")
frame = Frame(window)
frame.pack(expand=True, fill=BOTH)
button_silinder = Button(frame, text="Silinder", command=silider)
button_silinder.grid(row=0, column=0, padx=20, pady=20)
button_rectangle = Button(frame, text="Ristkülik", command=rectangle)
button_rectangle.grid(row=0, column=1, padx=20, pady=20)
button_stadium = Button(frame, text="Staadion", command=stadium)
button_stadium.grid(row=0, column=2, padx=20, pady=20)



window.mainloop()

