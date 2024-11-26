from datetime import datetime,date
from typing import NamedTuple
import csv
from collections import defaultdict,Counter

Pelicula = NamedTuple(
    "Pelicula",
    [("fecha_estreno", date), 
    ("titulo", str), 
    ("director", str), 
    ("generos",list[str]),
    ("duracion", int),
    ("presupuesto", int), 
    ("recaudacion", int), 
    ("reparto", list[str])
    ]
)

def lee_peliculas(ruta:str)->list[Pelicula]:
    with open (ruta, encoding="utf-8") as f:
        res = []
        lector = csv.reader(f,delimiter=";")
        next(lector)
        for fechae,titulo,director,generos,duracion,presupuesto,recaudacion,reparto in lector:
            fechae = datetime.strptime(fechae,"%d/%m/%Y").date()
            generos = parsea_lista(generos)
            duracion=int(duracion)
            presupuesto=int(presupuesto)
            recaudacion=int(recaudacion)
            reparto= parsea_lista(reparto)
            res.append(Pelicula(fechae,titulo,director,generos,duracion,presupuesto,recaudacion,reparto))
        return res

def parsea_lista (cadena:str)->list[str]:
    res=[]
    for troxo in cadena.split(","):
        res.append(troxo.strip())
    return res

def pelicula_mas_ganancias(lista:list[Pelicula],genero:str =None)->tuple[str,int]: 
    """
    Recibe una lista de tuplas de tipo Pelicula y una cadena de texto genero, con valor por defecto None, 
    y devuelve el título y las ganancias de la película con mayores ganancias, de entre aquellas películas que tienen 
    entre sus géneros el genero indicado. Si el parámetro genero es None, se busca la película con mayores ganancias, 
    sin importar sus géneros. Las ganancias de una película se calculan como la diferencia entre la recaudación 
    y el presupuesto.
    """
    listaf =  []
    for pelicula in lista:
        if genero == None or genero in pelicula.generos:
            listaf.append((pelicula.titulo,(pelicula.recaudacion-pelicula.presupuesto)))
    return max(listaf,key=lambda x: x[1])

    if genero == None:
            listaf = lista[:]
    else:
        for pelicula in lista:
            if genero in pelicula.generos:
                listaf.append(pelicula)
    maximo = max(listaf,key= lambda x:(x.recaudacion-x.presupuesto))

def media_presupuesto_por_genero(lista:list[Pelicula])->dict[str,float]: 
    """
    Recibe una lista de tuplas de tipo Pelicula y devuelve un diccionario en el que las claves son los distintos géneros 
    y los valores son la media de presupuesto de las películas de cada género.
    """
    #generos = defaultdict(lambda :(0,0))
    generos = {}
    for pelicula in lista:
        for genero in pelicula.generos:
            if genero not in generos:
                generos[genero]= (0, 0)
            generos[genero]= (generos[genero][0] + pelicula.presupuesto, generos[genero][1]+1)
    
    generosfinales = {}
    for gener,presupuestos in generos.items():
        generosfinales[gener]=presupuestos[0]/presupuestos[1]
    return generosfinales
        
def peliculas_por_actor(peliculas:list[Pelicula],ano_inicial:int=None,ano_final:int=None)->dict[str,int]: 
    """
    Recibe una lista de tuplas de tipo Pelicula y dos enteros año_inicial y año_final, con valor por defecto None, 
    y devuelve un diccionario en el que las claves son los nombres de los actores y actrices, 
    y los valores son el número de películas, estrenadas entre año_inicial y año_final (ambos incluidos), 
    en que ha participado cada actor o actriz. Si año_inicial o año_final son None, 
    se contarán las películas sin filtrar por año inicial o final, respectivamente.
    """
    actores = defaultdict(int)
    for pelicula in peliculas:
        if (ano_inicial == None or ano_inicial <=pelicula.fecha_estreno.year) and (ano_final == None or ano_final >= pelicula.fecha_estreno.year):
            for actor in pelicula.reparto:
                actores[actor]+=1
    return actores

def actores_mas_frecuentes(lista:list[Pelicula],n:int,ano_inicial:int=None,ano_final:int=None): 
    """
    Recibe una lista de tuplas de tipo Pelicula, un entero n y dos enteros año_inicial y año_final, 
    con valor por defecto None, y devuelve una lista con los n actores o actrices que han participado 
    en más películas estrenadas entre año_inicial y año_final (ambos incluidos). 
    La lista de actores o actrices debe estar ordenada alfabéticamente. Si año_inicial o año_final son None, 
    se contarán las películas sin filtrar por año inicial o final, respectivamente. 
    Haga uso de la función peliculas_por_actor para implementar esta función.
    """
    actores = (peliculas_por_actor(lista,ano_inicial,ano_final).items())
    actores.sort(key=lambda x:x[1])
    return sorted(actores[:n][0])
    #TENGO QUE TRANSFORMAR ACTORES DE DICT ITEMS EN LISTA DE TUPLAS