import sqlite3
import imdb

# creating instance of IMDb
ia = imdb.IMDb()
conexion = sqlite3.connect('peliculas.db')

#top 250
top250 = ia.get_top250_movies()
c = conexion.cursor()
generos=""

try:
    c.execute("SELECT * FROM pelis")

except:
    c.execute("CREATE TABLE pelis (ids int, generos text, titulo text)")

for movie_count in range(0, 249):
    # First, retrieve the movie object using its ID
    movie = ia.get_movie(top250[movie_count].movieID) #obtiene ID
    #busqueda = ia.search_keyword("happiness","peaceful")
  

    #Print movie title and genres
    #print(movie['title'])
    id = movie.movieID
    movieGenres= movie['genres']
    titulo = movie['title']
    for i in movieGenres:
        generos = generos + i+","
    print(movie.movieID)
    print(titulo)
    print(movieGenres)
    print(generos)
    c.execute("INSERT INTO pelis (ids, generos, titulo) values (?, ?, ?)", (id, generos, titulo))
    conexion.commit()

    generos = ""


# Leyendo todos los registros
c.execute('SELECT * FROM pelis')

# Ciclo para imprimir todos los registros
print('Contenido de tabla REDES:')

registros = c.fetchall()
for ciclo in registros:
    print(ciclo)
    

   
