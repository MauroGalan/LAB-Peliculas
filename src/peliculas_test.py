from peliculas import *

def test_lee_peliculas(ruta):
    datos = lee_peliculas(ruta)
    print(f"Los primeros tres elementos son: {datos[:3]}")
    print(f"Se han leído {len(datos)} registros")

def test_peliculas_mas_ganancias(ruta,genero=None):
    datos = lee_peliculas(ruta)
    pelicula = pelicula_mas_ganancias(datos,genero)
    print(f"La película con más ganancias del género {genero} es {pelicula}")

def test_media_presupuesto_por_genero(ruta):
    datos = lee_peliculas(ruta)
    medias = media_presupuesto_por_genero(datos)
    print(f"La media de presupuesto por cada género es {medias}")

def test_peliculas_por_actor(ruta,anoi,anof):
    datos = lee_peliculas(ruta)
    actores = peliculas_por_actor(datos,anoi,anof)
    print(f"Las películas realizadas por cada actor son {actores}")

if __name__ == "__main__":
    #test_lee_peliculas("data/peliculas.csv")
    #test_peliculas_mas_ganancias("data/peliculas.csv")
    #test_media_presupuesto_por_genero("data/peliculas.csv")
    test_peliculas_por_actor("data/peliculas.csv",1995,2015)
    print(actores_mas_frecuentes(lee_peliculas("data/peliculas.csv"),3,1995,2015))
