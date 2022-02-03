import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import clases.third as third
import clases.fourth as fourth
#from second import *
emociones = third.selecciones_S

class FifthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='blue')

        print("Página 5")
                
        path = Image.open('img/fondos/fondo_tania.png')
        img = ImageTk.PhotoImage(path)
        fondo = Label(self, image=img)
        fondo.image = img
        fondo.place(x=0, y=0)

        def ver():
            if (len(emociones)!= 0):
                archi1= "datos.txt"
                with open(archi1, "r", encoding="utf-8") as archivo:
                    frase=archivo.read()
                    titulos=frase.split("\n")
                print(titulos)
                
                
                """path = 'Imagen'+str(i+1)+'.jpg'
                    img = ImageTk.PhotoImage(Image.open(path))
                    if (i+1) == 1:
                        img1 = img
                        fondo = tk.Label(self, image=img1)
                        fondo.pack()
                    if (i+1) == 2:
                        img2 = img
                        fondo2 = tk.Label(self, image=img2)
                        fondo2.pack()
                    if (i+1) == 3:
                        img3 = img
                        fondo3 = tk.Label(self, image=img3)
                        fondo3.pack()
                    if (i+1) == 4:
                        img4 = img
                        fondo4 = tk.Label(self, image=img4)
                        fondo4.pack()
                    if (i+1) == 5:
                        img5 = img
                        fondo5 = tk.Label(self, image=img5)
                        fondo5.pack() 
                """
                #1 titulo y su imagen
                if (len(titulos) > 0):
                    self.etiqueta = tk.Label(self, text=titulos[0], font ="Helvetica 25", fg="white", bg="black")   
                    #self.etiqueta.place(relx=400,rely=460)     
                    self.etiqueta.pack()
                    path1 = Image.open('Imagen1.jpg')
                    img1 = ImageTk.PhotoImage(path1)
                    fondo1 = Label(self, image=img1)
                    fondo1.image = img1
                    #fondo1.place(x=10, y=10)
                    fondo1.pack()

                if (len(titulos) >= 3):
                    print(len(titulos))
                    #1 titulo y su imagen
                    self.etiqueta = tk.Label(self, text=titulos[1], font ="Helvetica 25", fg="white", bg="black")   
                    #self.etiqueta.place(relx=600,rely=460)     
                    self.etiqueta.pack()
                    path2 = Image.open('Imagen2.jpg')
                    img2 = ImageTk.PhotoImage(path2)
                    fondo2 = Label(self, image=img2)
                    fondo2.image = img2
                    #fondo2.place(x=10, y=10)
                    fondo2.pack()

                if (len(titulos) >= 4):
                    #1 titulo y su imagen
                    self.etiqueta = tk.Label(self, text=titulos[2], font ="Helvetica 25", fg="white", bg="black")   
                    #self.etiqueta.place(relx=600,rely=460)     
                    self.etiqueta.pack()
                    path3 = Image.open('Imagen3.jpg')
                    img3 = ImageTk.PhotoImage(path3)
                    fondo3 = Label(self, image=img3)
                    fondo3.image = img3
                    #fondo2.place(x=10, y=10)
                    fondo3.pack()
                ButtonShow['state']='disabled'
            
        
                
                

        
              
        ButtonShow = tk.Button(self, text="Ver mis recomendaciones", font=("Arial", 15),command=ver)
        
        ButtonShow.place(x=250, y=650)

        ButtonQuit = tk.Button(self, text="Salir", font=("Arial", 15), command=self.quit )
        #Button['state']=DISABLED (OTRA FORMA DE DESHABLITAR)
        ButtonQuit.place(x=620, y=650)
        #ButtonQuit['state']='disabled'