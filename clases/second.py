import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import clases.third as third
import clases.first as first
import clases.fourth as fourth

selecciones =[]


class SecondPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='green')
        print("Página 2")

        path = Image.open('img/fondos/fondo_edu3.png')
        img = ImageTk.PhotoImage(path)
        fondo = Label(self, image=img)
        fondo.image = img
        fondo.place(x=0, y=0)

        #selecciones =[]

        #Funciones para obtener el valor de los botones                
        def valorAccion():
            selecciones.append("Action") 
            btnAccion['state']='disabled'
            listo()
            print(selecciones)            
            print("ACCION")
        
        def valorTerror():
            selecciones.append("Horror") 
            btnTerror['state']='disabled'
            listo()
            print(selecciones)            
            print("TERROR")
        
        def valorDrama():
            selecciones.append("Drama") 
            btnDrama['state']='disabled'
            listo()
            print(selecciones)            
            print("DRAMA")

        def valorComedia():
            selecciones.append("Comedy") 
            btnComedia['state']='disabled'
            listo()
            print(selecciones)            
            print("COMEDIA")
        
        def valorSuspenso():
            selecciones.append("Thriller") 
            btnSuspenso['state']='disabled'
            listo()
            print(selecciones)            
            print("SUSPENSO")
        
        def valorCrimen():
            selecciones.append("Crime") 
            btnCrimen['state']='disabled'
            listo()
            print(selecciones)            
            print("CRIMEN")
        
        def valorFantasia():
            selecciones.append("Fantasy") 
            btnFantasia['state']='disabled'
            listo()
            print(selecciones)            
            print("FANTASIA")

        def valorMusical():
            selecciones.append("Musical")
            btnMusical['state']='disabled' 
            listo()
            print(selecciones)            
            print("MUSICAL")


        #Creación de imágenes

        #imagen1
        path1=Image.open('img/GENEROS_PELIS/1.png')
        img1=ImageTk.PhotoImage(path1)
        #imagen2
        path2 =Image.open('img/GENEROS_PELIS/4.png')
        img2=ImageTk.PhotoImage(path2)
        #imagen3
        path3=Image.open('img/GENEROS_PELIS/7.png')
        img3=ImageTk.PhotoImage(path3)
        #imagen4
        path4 =Image.open('img/GENEROS_PELIS/10.png')
        img4=ImageTk.PhotoImage(path4)
        #imagen5
        path5=Image.open('img/GENEROS_PELIS/13.png')
        img5=ImageTk.PhotoImage(path5)
        #imagen6
        path6 =Image.open('img/GENEROS_PELIS/16.png')
        img6=ImageTk.PhotoImage(path6)
        #imagen7
        path7=Image.open('img/GENEROS_PELIS/19.png')
        img7=ImageTk.PhotoImage(path7)
        #imagen8
        path8 =Image.open('img/GENEROS_PELIS/22.png')
        img8=ImageTk.PhotoImage(path8)



        #lista de imagenes
        images = [img1,img2,img3,img4,img5,img6,img7,img8]

        #------Boton1 = Accion
        btnAccion = tk.Button(self, text="Accion", command=valorAccion)
        btnAccion.configure(image=images[0])
        btnAccion.image=images[0] #configurar la imagen en el boton e indicarle a su propiedad "image" la imagen
        btnAccion.place(x=50, y=200)

        #------Boton2 = Terror
        btnTerror = tk.Button(self, text="Terror", command=valorTerror)
        btnTerror.configure(image=images[1])
        btnTerror.image=images[1] #configurar la imagen en el boton e indicarle a su propiedad "image" la imagen
        btnTerror.place(x=250, y=200)

        #------Boton3 = Comedia
        btnDrama = tk.Button(self, text="Drama", command=valorDrama)
        btnDrama.configure(image=images[2])
        btnDrama.image=images[2] #configurar la imagen en el boton e indicarle a su propiedad "image" la imagen
        btnDrama.place(x=450, y=200)

        #------Boton4 = Accion
        btnComedia = tk.Button(self, text="Comedia", command=valorComedia)
        btnComedia.configure(image=images[3])
        btnComedia.image=images[3] #configurar la imagen en el boton e indicarle a su propiedad "image" la imagen
        btnComedia.place(x=650, y=200)

        #segunda fila

        #------Boton1 =     Suspenso
        btnSuspenso = tk.Button(self, text="Suspenso", command=valorSuspenso)
        btnSuspenso.configure(image=images[4])
        btnSuspenso.image=images[4] #configurar la imagen en el boton e indicarle a su propiedad "image" la imagen
        btnSuspenso.place(x=50, y=400)

        #------Boton2 = Crimen
        btnCrimen = tk.Button(self, text="Crimen", command=valorCrimen)
        btnCrimen.configure(image=images[5])
        btnCrimen.image=images[5] #configurar la imagen en el boton e indicarle a su propiedad "image" la imagen
        btnCrimen.place(x=250, y=400)

        #------Boton3 = Fantasia
        btnFantasia = tk.Button(self, text="Fantasia", command=valorFantasia)
        btnFantasia.configure(image=images[6])
        btnFantasia.image=images[6] #configurar la imagen en el boton e indicarle a su propiedad "image" la imagen
        btnFantasia.place(x=450, y=400)

        #------Boton4 = Musical
        btnMusical = tk.Button(self, text="Musical", command=valorMusical)
        btnMusical.configure(image=images[7])
        btnMusical.image=images[7] #configurar la imagen en el boton e indicarle a su propiedad "image" la imagen
        btnMusical.place(x=650, y=400)


        def listo():
            if (len(selecciones)>0):                
                ButtonDelete['state']='active'
            if (len(selecciones)!= 3):
                ButtonNext['state']='disabled'
                #ButtonDelete['state']='disabled'            
            else:
                ButtonDelete['state']='active'
                ButtonNext['state']='active'

                #deshabilitar los demás
                btnAccion['state']='disabled'
                btnComedia['state']='disabled'
                btnCrimen['state']='disabled'
                btnDrama['state']='disabled'
                btnFantasia['state']='disabled'
                btnSuspenso['state']='disabled'
                btnMusical['state']='disabled'
                btnTerror['state']='disabled'
        
        def borrar():
            selecciones.clear()
            print(selecciones)
            # if (len(selecciones_S)!= 3):
            #     ButtonNext['state']='disabled'
            # else:
            ButtonNext['state']='disabled'
            #habilitar los demás
            btnAccion['state']='active'
            btnComedia['state']='active'
            btnCrimen['state']='active'
            btnDrama['state']='active'
            btnFantasia['state']='active'
            btnSuspenso['state']='active'
            btnMusical['state']='active'
            btnTerror['state']='active'
            
            selecciones.clear()






        #------Botones de control

        ButtonNext = tk.Button(self, text="Siguiente", font=("Arial", 15), command=lambda: controller.show_frame(third.ThirdPage))
        ButtonNext.place(x=800, y=650)

        # ButtonReady = tk.Button(self, text="Listo", font=("Arial", 15), command=listo)
        # ButtonReady.place(x=350, y=650)

        ButtonDelete = tk.Button(self, text="Borrar selección", font=("Arial", 15), command=borrar)
        ButtonDelete['state']='disabled'
        ButtonDelete.place(x=380, y=650)

        ButtonBack = tk.Button(self, text="Regresar", font=("Arial", 15), command=lambda: controller.show_frame(first.FirstPage))
        ButtonBack.place(x=30, y=650)

      