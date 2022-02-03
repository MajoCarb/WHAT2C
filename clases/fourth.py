import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import clases.third as third
import clases.second as second
import clases.fifth as fifth
import clases.fourth as fourth
import sqlite3
from bs4 import BeautifulSoup
from tkinter import ttk, PhotoImage, Label
import requests
#imdb things
import imdb
ia = imdb.IMDb()
conexion = sqlite3.connect('peliculas.db')

c = conexion.cursor()
c.execute('SELECT generos FROM pelis')
registros = c.fetchall()
c.execute('SELECT ids FROM pelis')
id = c.fetchall()


resultados = []
emociones = third.selecciones_S
generos1 = second.selecciones
recomendaciones =[]
seleccion1 = []

        

    
class FourthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='Tomato')

        resultados=[]
        #primer_emocion = recibirSeleccionesS[0]
        #label
        
        print("Página 4")
        recomendacion1=[]
        print("esto esta dentro de la clase: ",recomendacion1)
        
        path = Image.open('img/fondos/fondo_tania.png')
        img = ImageTk.PhotoImage(path)
        fondo = Label(self, image=img)
        fondo.image = img
        fondo.place(x=0, y=0)
       
        
        def recibirSeleccionesS():
            ButtonNext['state']='active'
            ButtonSearch['state']='disabled'
            print("lista de emociones: ",emociones)
            print("lista de generos1: ",generos1)
            print("lista de selecciones: ",seleccion1)
            if (len(emociones)!= 0):
                for i in emociones:
                    seleccion1.append(i)
            if (len(generos1)!= 0):
                for i in generos1:
                    seleccion1.append(i)
            

            for i in range(len(registros)):
                generos_crudos = registros[i][0]
                generos = generos_crudos.split(sep=",")
                generos.pop(len(generos)-1)
                print(generos)
                for genero in generos:
                    temp = []
                    temp = list(id[i])
                    if(genero in seleccion1):
                        recomendaciones.append(temp[0])
            print("lista de recomendaciones: ",recomendaciones)
            
            num_repeticiones = []
            repetidos = []

            contador = 0
            for i in recomendaciones:
                for j in recomendaciones:
                    if (i == j):
                        contador+=1
                contador = contador -1
                if contador >= 1:
                    if (i not in num_repeticiones):
                        num_repeticiones.append(i)
                        repetidos.append(contador)
                contador = 0

            n = 0
            m = 0
            temp = 0
            pais1 = 0
            pais2 = 0
            for i in repetidos:
                for j in repetidos:
                    if i > j :
                        temp = i
                        i = j
                        repetidos[n] = i
                        repetidos[m] = temp
                        pais1 = num_repeticiones[n]
                        pais2 = num_repeticiones[m]
                        num_repeticiones[n] = pais2
                        num_repeticiones[m] = pais1

                    m+=1
                m=0
                n+=1
            print ("repetidos: ",repetidos)
            
            print ("lista Final: ",num_repeticiones)
            titulos = []
            envio = ""
            for peli in num_repeticiones[0:3]:

                c.execute('SELECT titulo FROM pelis WHERE ids=?',(peli, ))
                titulo = c.fetchall()
                temp = []
                temp = list(titulo[0])
                titulos.append(temp[0])
                #print("Titulo:",titulo)
                print("Nombre:",temp)
                envio=temp
            print("Te recomendamos: ",titulos)
            
        
            if (len(emociones)!= 0):
                archi1=open("datos.txt","w")
                for titulo in titulos:
                    archi1.write(titulo+"\n")
                archi1.close() 
            
            #Este for crea las imagenes y las guarda en nuestra carpeta
            for i, ids in enumerate(num_repeticiones[0:3]):  
                movie = ia.get_movie(ids)
                imagen  = movie['cover url']
                la_imagen = requests.get(imagen)

                nombreImagen ='Imagen'+str(i+1)+'.jpg'
                with open(nombreImagen, 'wb')as imagenNoticia:
                    imagenNoticia.write(la_imagen.content)

        if (len(emociones)!= 0):
            for i in emociones:   
                
                seleccion1.append(i)
        if (len(generos1)!= 0):
            for i in generos1:
                seleccion1.append(i)   


        ButtonNext = tk.Button(self, text="Siguiente", font=("Arial", 15), command=lambda: controller.show_frame(fifth.FifthPage))
        ButtonNext.place(x=800, y=650)
        ButtonNext['state']='disabled'


        ButtonSearch = tk.Button(self, text="Click aquí para comenzar búsqueda \ny luego en Siguiente", font=("Arial", 25), command=recibirSeleccionesS)
        ButtonSearch.place(x=210, y=340)

        # Button = tk.Button(self, text="Regresar(3)", font=("Arial", 15), command=lambda: controller.show_frame(third.ThirdPage))
        # Button.place(x=30, y=650)
        
    
    