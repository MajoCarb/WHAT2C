import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import clases.second as second
import clases.fourth as fourth

selecciones_S =[]

class ThirdPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='Tomato')

        print("Página 3")
        
        path = Image.open('img/fondos/fondo_emociones.png')
        img = ImageTk.PhotoImage(path)
        fondo = Label(self, image=img)
        fondo.image = img
        fondo.place(x=0, y=0)

        # selecciones_S =[]

        #Funciones para obtener el valor de los botones
                    
        def valorTristeza():
            selecciones_S.append("War")
            btnTristeza['state']='disabled' 
            print(selecciones_S)
            listo()
            print("TRISTEZA")
        
        def valorFelicidad():
            selecciones_S.append("Family")
            btnFelicidad['state']='disabled'
            listo()
            print(selecciones_S)
            print("FELICIDAD")
        
        def valorEnojo():
            selecciones_S.append("History")
            btnEnojo['state']='disabled' 
            listo()
            print(selecciones_S)
            print("ENOJO")

        def valorAnsiedad():
            selecciones_S.append("Film Noir") 
            btnAnsiedad['state']='disabled'
            listo()
            print(selecciones_S)
            print("ANSIEDAD")
        
        def valorMiedo():
            selecciones_S.append("Mistery")
            btnMiedo['state']='disabled' 
            listo()
            print(selecciones_S)
            print("MIEDO")
        
        def valorInquietud():
            selecciones_S.append("Adventure")
            btnInquietud['state']='disabled'
            listo() 
            print(selecciones_S)
            print("INQUIETUD")
        
        def valorCalma():
            selecciones_S.append("Animation") 
            btnCalma['state']='disabled'
            listo()
            print(selecciones_S)
            print("CALMA")

        def valorAmor():
            selecciones_S.append("Romance") 
            btnAmor['state']='disabled'
            listo()
            print(selecciones_S)
            print("AMOR")


        #Creación de imágenes

        #imagen1
        path1=Image.open('img/emociones/25.png')
        img1=ImageTk.PhotoImage(path1)
        #imagen2
        path2 =Image.open('img/emociones/26.png')
        img2=ImageTk.PhotoImage(path2)
        #imagen3
        path3=Image.open('img/emociones/27.png')
        img3=ImageTk.PhotoImage(path3)
        #imagen4
        path4 =Image.open('img/emociones/28.png')
        img4=ImageTk.PhotoImage(path4)
        #imagen5
        path5=Image.open('img/emociones/29.png')
        img5=ImageTk.PhotoImage(path5)
        #imagen6
        path6 =Image.open('img/emociones/30.png')
        img6=ImageTk.PhotoImage(path6)
        #imagen7
        path7=Image.open('img/emociones/31.png')
        img7=ImageTk.PhotoImage(path7)
        #imagen8
        path8 =Image.open('img/emociones/32.png')
        img8=ImageTk.PhotoImage(path8)



        #lista de imagenes
        images = [img1,img2,img3,img4,img5,img6,img7,img8]

        #------Boton1 = Accion
        btnTristeza = tk.Button(self, text="Tristeza", command=valorTristeza)
        btnTristeza.configure(image=images[0])
        btnTristeza.image=images[0] #configurar la imagen en el boton e indicarle a su propiedad "image" la imagen
        btnTristeza.place(x=50, y=200)

        #------Boton2 = Terror
        btnFelicidad = tk.Button(self, text="Felicidad", command=valorFelicidad)
        btnFelicidad.configure(image=images[1])
        btnFelicidad.image=images[1] #configurar la imagen en el boton e indicarle a su propiedad "image" la imagen
        btnFelicidad.place(x=250, y=200)

        #------Boton3 = Comedia
        btnEnojo = tk.Button(self, text="Enojo", command=valorEnojo)
        btnEnojo.configure(image=images[2])
        btnEnojo.image=images[2] #configurar la imagen en el boton e indicarle a su propiedad "image" la imagen
        btnEnojo.place(x=450, y=200)

        #------Boton4 = Accion
        btnAnsiedad = tk.Button(self, text="Ansiedad", command=valorAnsiedad)
        btnAnsiedad.configure(image=images[3])
        btnAnsiedad.image=images[3] #configurar la imagen en el boton e indicarle a su propiedad "image" la imagen
        btnAnsiedad.place(x=650, y=200)

        #segunda fila

        #------Boton1 =     Suspenso
        btnMiedo = tk.Button(self, text="Miedo", command=valorMiedo)
        btnMiedo.configure(image=images[4])
        btnMiedo.image=images[4] #configurar la imagen en el boton e indicarle a su propiedad "image" la imagen
        btnMiedo.place(x=50, y=400)

        #------Boton2 = Crimen
        btnInquietud = tk.Button(self, text="Inquietud", command=valorInquietud)
        btnInquietud.configure(image=images[5])
        btnInquietud.image=images[5] #configurar la imagen en el boton e indicarle a su propiedad "image" la imagen
        btnInquietud.place(x=250, y=400)

        #------Boton3 = Fantasia
        btnCalma = tk.Button(self, text="Calma", command=valorCalma)
        btnCalma.configure(image=images[6])
        btnCalma.image=images[6] #configurar la imagen en el boton e indicarle a su propiedad "image" la imagen
        btnCalma.place(x=450, y=400)

        #------Boton4 = Musical
        btnAmor = tk.Button(self, text="Amor", command=valorAmor)
        btnAmor.configure(image=images[7])
        btnAmor.image=images[7] #configurar la imagen en el boton e indicarle a su propiedad "image" la imagen
        btnAmor.place(x=650, y=400)

        def listo():
            if (len(selecciones_S)!= 1):
                ButtonNext['state']='disabled'
                ButtonDelete['state']='disabled'
            else:
                ButtonDelete['state']='active'
                ButtonNext['state']='active'
                #deshabilitar los demás
                btnAmor['state']='disabled'
                btnCalma['state']='disabled'
                btnAnsiedad['state']='disabled'
                btnEnojo['state']='disabled'
                btnFelicidad['state']='disabled'
                btnInquietud['state']='disabled'
                btnMiedo['state']='disabled'
                btnTristeza['state']='disabled'
        
        def borrar():
            selecciones_S.clear()
            print(selecciones_S)
            # if (len(selecciones_S)!= 3):
            #     ButtonNext['state']='disabled'
            # else:
            ButtonNext['state']='disabled'
            #deshabilitar los demás
            btnAmor['state']='active'
            btnCalma['state']='active'
            btnAnsiedad['state']='active'
            btnEnojo['state']='active'
            btnFelicidad['state']='active'
            btnInquietud['state']='active'
            btnMiedo['state']='active'
            btnTristeza['state']='active'
            
            selecciones_S.clear()


        ButtonNext = tk.Button(self, text="Siguiente", font=("Arial", 15), command=lambda: controller.show_frame(fourth.FourthPage))
        ButtonNext['state']='disabled'
        ButtonNext.place(x=800, y=650)
              
        ButtonDelete = tk.Button(self, text="Borrar selección", font=("Arial", 15), command=borrar)
        ButtonDelete['state']='disabled'
        ButtonDelete.place(x=380, y=650)

        ButtonBack = tk.Button(self, text="Regresar", font=("Arial", 15), command=lambda: controller.show_frame(second.SecondPage) )
        #Button['state']=DISABLED (OTRA FORMA DE DESHABLITAR)
        ButtonBack.place(x=30, y=650)

        
            

        