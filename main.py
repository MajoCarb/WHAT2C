"""re
Maria Jose Carbajal Alonzo
Ana Tania Medina Espinoza
Jose Eduardo Rodriguez Gallegos
Enil Perales Calderon
"""
from clases.fourth import FourthPage
import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
import os
from PIL import ImageTk, Image
from clases.first import FirstPage
from clases.second import SecondPage
from clases.third import ThirdPage
from clases.fifth import FifthPage
import sqlite3

prueba= "esto está fuera de Application"

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # crea una ventana
        window = tk.Frame(self)
        window.pack()
        prueba2= "esto está dentro de Application"
        self.prueba3 = "esto está dentro de Application y es variable de clase"

        window.grid_rowconfigure(0, minsize=700)
        window.grid_columnconfigure(0, minsize=900)

        self.frames = {}
        #crea un diccionario con todas las clases
        for F in (FirstPage, SecondPage, ThirdPage,FourthPage,FifthPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(FirstPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Application")
    
app = Application()
app.maxsize(900, 700)
app.mainloop()
