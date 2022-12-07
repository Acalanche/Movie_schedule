"""
Ejercicio nivel 2: Agenda de peliculas.
Módulo de cálculos.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.
@author: Cupi2

NOTA IMPORTANTE PARA TENER EN CUENTA EN TODAS LAS FUNCIONES DE ESTE MODULO:
        Los diccionarios de pelicula tienen las siguientes parejas de clave-valor:
            - nombre (str): Nombre de la pelicula agendada.
            - genero (str): Generos de la pelicula separados por comas.
            - duracion (int): Duracion en minutos de la pelicula
            - anio (int): Anio de estreno de la pelicula
            - clasificacion (str): Clasificacion de restriccion por edad
            - hora (int): Hora de inicio de la pelicula
            - dia (str): Indica que día de la semana se planea ver la película
"""

def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int, 
                  clasificacion: str, hora: int, dia: str) -> dict:
    """Crea un diccionario que representa una nueva película con toda su información 
       inicializada.
    Parámetros:
        nombre (str): Nombre de la pelicula agendada.
        genero (str): Generos de la pelicula separados por comas.
        duracion (int): Duracion en minutos de la pelicula
        anio (int): Anio de estreno de la pelicula
        clasificacion (str): Clasificacion de restriccion por edad
        hora (int): Hora a la cual se planea ver la pelicula, esta debe estar entre 
                    0 y 2359
        dia (str): Dia de la semana en el cual se planea ver la pelicula.
    Retorna:
        dict: Diccionario con los datos de la pelicula
    """
    pelicula={"nombre":nombre,"genero":genero,"duracion":duracion,"anio":anio,"clasificacion":clasificacion,"hora":hora,"dia":dia}
    return pelicula 


def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict, p3: dict, p4: dict,  p5: dict) -> dict:
    """Encuentra en cual de los 5 diccionarios que se pasan por parametro esta la 
       pelicula cuyo nombre es dado por parametro.
       Si no se encuentra la pelicula se debe retornar None.
    Parametros:
        nombre_pelicula (str): El nombre de la pelicula que se desea encontrar.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: Diccionario de la pelicula cuyo nombre fue dado por parametro. 
        None si no se encuentra una pelicula con ese nombre.
    """
    n_p=None
    nombre_pelicula=input("ingrese el nombre de la pelicula que desea ver")
    if nombre_pelicula.lower()==p1["nombre"].lower():
        n_p=p1
    elif nombre_pelicula.lower()==p2["nombre"].lower():
        n_p=p2
    elif nombre_pelicula.lower()==p3["nombre"].lower():
        n_p=p3
    elif nombre_pelicula.lower()==p4["nombre"].lower():
        n_p=p4
    elif nombre_pelicula.lower()==p5["nombre"].lower():
        n_p=p5
    
    
    return n_p

def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    """Encuentra la pelicula de mayor duracion entre las peliculas recibidas por
       parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: El diccionario de la pelicula de mayor duracion
    """
    pelicula_mas_larga = p1
    duracion_mas_larga = p1["duracion"]
    if (p2["duracion"] > duracion_mas_larga):
        pelicula_mas_larga = p2
        duracion_mas_larga = p2["duracion"]
    if (p3["duracion"] > duracion_mas_larga):
        pelicula_mas_larga = p3
        duracion_mas_larga = p3["duracion"]
    if (p4["duracion"] > duracion_mas_larga):
        pelicula_mas_larga = p4
        duracion_mas_larga = p4["duracion"]
    if (p5["duracion"] > duracion_mas_larga):
        pelicula_mas_larga = p5
        duracion_mas_larga = p5["duracion"]
    return pelicula_mas_larga


def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> str:
    """Calcula la duracion promedio de las peliculas que entran por parametro. 
       Esto es, la duración total de todas las peliculas dividida sobre el numero de peliculas. 
       Retorna la duracion promedio en una cadena de formato 'HH:MM' ignorando los posibles decimales.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        str: la duracion promedio de las peliculas en formato 'HH:MM'
    """
    duracion_total=int(p1["duracion"])+int(p2["duracion"])+int(p3["duracion"])+int(p4["duracion"])+int(p5["duracion"])
    promedio=duracion_total/5
    horas=int(promedio/60)
    minutos=int(((promedio/60)-horas)*60)
    
    return "0{}:{}".format(horas,minutos)

def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, anio: int) -> str:
    """Busca entre las peliculas cuales tienen como anio de estreno una fecha estrictamente
       posterior a la recibida por parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
        anio (int): Anio limite para considerar la pelicula como estreno.
    Retorna:
        str: Una cadena con el nombre de la pelicula estrenada posteriormente a la fecha recibida. 
        Si hay mas de una pelicula, entonces se retornan los nombres de todas las peliculas 
        encontradas separadas por comas. Si ninguna pelicula coincide, retorna "Ninguna".
    """
    peliculas = " "
    # variable que determina si se encontro alguna pelicula con las caracteristicas especificadas
    encontrar =  False
    if anio <=p1["anio"] :
        peliculas += p1["nombre"] 
        encontrar = False
    if anio <= p2["anio"] :
        peliculas +=  ", "+ p2["nombre"]
        encontrar = False
    if anio <= p3["anio"] :
        peliculas += ", "+p3["nombre"]
        encontrar = False
    if anio <= p4["anio"] :
        peliculas +=", "+p4["nombre"]
        encontrar = False
    if anio <= p5["anio"] :
        peliculas +=", "+p5["nombre"]
        encontrar = False

    else:
        if encontrar:
            peliculas="Ninguna pelicula coincide con el año indicado"
    return peliculas


def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> int:
    """Indica cuantas peliculas de clasificación '18+' hay entre los diccionarios recibidos.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        int: Numero de peliculas con clasificacion '18+'
    """
    n_pel=0
    if p1["clasificacion"]=="18+":
        n_pel+=1
    if p2["clasificacion"]=="18+":
        n_pel+=1
    if p3["clasificacion"]=="18+":
        n_pel+=1
    if p4["clasificacion"]=="18+":
        n_pel+=1
    if p5["clasificacion"]=="18+":
        n_pel+=1
    return n_pel

def reagendar_pelicula(peli:dict, nueva_hora: int, nuevo_dia: str, 
                       control_horario: bool, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->bool: 
    """Verifica si es posible reagendar la pelicula que entra por parametro. Para esto verifica
       si la nueva hora y el nuevo dia no entran en conflicto con ninguna otra pelicula, 
       y en caso de que el usuario haya pedido control horario verifica que se cumplan 
       las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula a reagendar
        nueva_hora (int): Nueva hora a la cual se quiere ver la pelicula
        nuevo_dia (str): Nuevo dia en el cual se quiere ver la pelicula
        control_horario (bool): Representa si el usuario quiere o no controlar
                                el horario de las peliculas.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        bool: True en caso de que se haya podido reagendar la pelicula, False de lo contrario.
    """
    reagendar=False
    
    if control_horario:
        if p1["hora"]!=nueva_hora and p1["dia"]!=nuevo_dia:
            reagendar=True
        elif p2["hora"]!=nueva_hora and p2["dia"]!=nuevo_dia:
            reagendar=True
        elif p3["hora"]!=nueva_hora and p3["dia"]!=nuevo_dia:
            reagendar=True
        elif p4["hora"]!=nueva_hora and p4["dia"]!=nuevo_dia:
            reagendar=True
        elif p5["hora"]!=nueva_hora and p5["dia"]!=nuevo_dia:
            reagendar=True

    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    return reagendar
    
def decidir_invitar(peli: dict, edad_invitado: int, autorizacion_padres: bool)->bool:
    """Verifica si es posible invitar a la persona cuya edad entra por parametro a ver la 
       pelicula que entra igualmente por parametro. 
       Para esto verifica el cumplimiento de las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula que se desea ver con el invitado
        edad_invitado (int): Edad del invitado con quien se desea ver la pelicula
        autorizacion_padres (bool): Indica si el invitado cuenta con la autorizacion de sus padres 
        para ver la pelicula
    Retorna:
        bool: True en caso de que se pueda invitar a la persona, False de lo contrario.
    """
    edad=0
    invita=True
    if peli["clasificacion"]=="todos":
        edad=0
        
    elif peli["clasificacion"]=="7+":
        edad=7
        
    elif peli["clasificacion"]=="13+":
        edad=13
        
    elif peli["clasificacion"]=="16+":
        edad=16
        
    elif peli["clasificacion"]=="18+":
        edad=18
        
        
        if edad>=edad_invitado and autorizacion_padres==True:
                invita=False
    return invita









