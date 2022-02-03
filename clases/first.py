import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import clases.second as second
#from second import *


class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='blue')

        print("Página 1")
                
        path = Image.open('img/fondos/what2c.png')
        img = ImageTk.PhotoImage(path)
        fondo = Label(self, image=img)
        fondo.image = img
        fondo.place(x=0, y=0)

        

        Button = tk.Button(self, text="Comenzar test (2)", font=("Arial", 15), command=lambda: controller.show_frame(second.SecondPage))
        #okey, la linea de arriba me decía (al correr este archivo, no el main) que ningún módulo contenía el atributo SecondPage. Por lo que tuve que importar el módulo que sí tuviera este "atributo", aunque realmente es una clase. Entonces importé class.second con el alias second, y a este alias le saqué su "atributo" SecondPage
        Button.place(x=600, y=350)