from curses.ascii import isdigit
import re
archivo = open('/home/javier/Escritorio/JulioVerne.bib', 'r', encoding='utf-8')
archivo_leido = archivo.read()

def presentacion():
    print("|            BIEVENIDO A JULIO VERNE 1.0                 |")
    print("|                                                        |")
    print("| 1- Años en que el autor publicó obras                  |")
    print("| 2- Años en que el autor no publicó obras               |")
    print("| 3- Años en que el autor publicó más obras              |")
    print("| 4- Título original más largo y año de publicación      |")
    print("| 5- Título original más corto y año de publicación      |")
    print("| 6- Título en castellano más largo y año de publicación |")
    print("| 7- Título en castellano más corto y año de publicación |")
    print("| 8- Las 10 palabras que más se repiten                  |")
    print("| 9- Promedio de palabras en los títulos originales      |")
    print("| 10- Promedio de palabras en los títulos en castellano  |")
    print("| 11- Lista de títulos idénticos en un idioma y otro     |")
    print("| 12- Lista de títulos donde aparecen números            |")
    print("| 13- Salir del programa                                 |")
    print() 


def lista_lineas(archivo_leido):
    lista_lineas = archivo_leido.splitlines()
    return lista_lineas

def lista_años(archivo_leido):
    lista_lineas_1 = lista_lineas(archivo_leido)
    lista_de_años = []
    for linea in lista_lineas_1:
        año = linea[0:4]
        año = int(año)
        lista_de_años.append(año)
    return lista_de_años

def lista_palabras(archivo_leido):
    lista_palabras = archivo_leido.split()
    for x in lista_palabras:
        if x.isdigit():
            lista_palabras.remove(x)
    return lista_palabras

#rango de años de publicaciones
def rango_años(archivo_leido):
    lista_lineas_1 = lista_lineas(archivo_leido)
    lista_de_años = []
    for linea in lista_lineas_1:
        año = linea[0:4]
        lista_de_años.append(año)
    sorted(lista_de_años)
    return  lista_de_años[0], lista_de_años[-1]
 
#print(rango_años(archivo_leido))


#años en los que el autor no publico obras
def anio_sin_obras(archivo_leido):
    lista_años_1 = lista_años(archivo_leido)
    lista_años_sin_repeticiones = []
    años_sin_obras= []
    for x in lista_años_1:
        if x not in lista_años_sin_repeticiones:
            lista_años_sin_repeticiones.append(x)
    control = lista_años_sin_repeticiones[0]
    while True:
        while control in lista_años_sin_repeticiones:
            control += 1
            if control not in lista_años_sin_repeticiones:
                años_sin_obras.append(control)
                control +=1
        break
    return años_sin_obras[:-1]

años_sin_obras = anio_sin_obras(archivo_leido)
#print(años_sin_obras)

#Año en el que el autor publicó mas obras y cuantas.
def anio_mas_obras(archivo_leido):
    lista_anios_1 = lista_años(archivo_leido)
    anios_cantidad_obras = {}
    resultado = {}
    for anio in lista_anios_1:
        if anio not in anios_cantidad_obras:
            anios_cantidad_obras[anio] = 1
        else:
            anios_cantidad_obras[anio] +=1
    contador = 1 
    
    for anio, cantidad in anios_cantidad_obras.items():
        if cantidad > contador:
            resultado [anio] = cantidad
            contador +=1
    return resultado

años_con_mas_obras = anio_mas_obras(archivo_leido)
#print(años_con_mas_obras

#titulos en castellano
def titulos_castellano_con_anios(archivo_leido):
    lista_lineas_1 = lista_lineas(archivo_leido)
    titulos_castellano_1 = []
    for linea in lista_lineas_1:
        titulos = linea[0:63].strip("\t").strip()
        titulos_castellano_1.append(titulos)
    return titulos_castellano_1

#print(titulos_castellano(archivo_leido))


#04.*Título castellano mas largo (en cantidad de carácteres) y su año de publicación.
def titulos_castellano_largo(archivo_leido):
    titulos_castellano_1 = titulos_castellano_con_anios(archivo_leido)
    titulo_mas_largo = ""
    anio_publicacion = ""
    caracteres = 0
    for titulo in titulos_castellano_1:
        if len(titulo) > caracteres:
            caracteres = len(titulo)
            titulo_mas_largo = titulo[5:]
            anio_publicacion = titulo[0:4]
    return titulo_mas_largo, caracteres, anio_publicacion

titulos = titulos_castellano_largo(archivo_leido)
#print(titulos)

#Título castellano mas corto (en cantidad de carácteres) y su año de publicación.
def titulo_castellano_corto(archivo_leido):
    todos_titulos = []
    titulo_corto = ""
    anio_publicacion = ""
    lista_lineas_1 = lista_lineas(archivo_leido)
    for titulos in lista_lineas_1:
            titulos = titulos[:63].strip("\t").strip()
            todos_titulos.append(titulos)
    cantidad_caracteres = 100
    for titulos in todos_titulos:
        if len(titulos[5:]) < cantidad_caracteres:
            cantidad_caracteres = len(titulos[5:])
            titulo_corto = titulos[5:]
            anio_publicacion = titulos[:4]
    return titulo_corto, cantidad_caracteres, anio_publicacion
 
titulo_corto = titulo_castellano_corto(archivo_leido)
#print(titulo_corto)

# Título original mas largo (en cantidad de carácteres) y su año de publicación.
def titulo_original_largo(archivo_leido):
    lista_lineas_1 = lista_lineas(archivo_leido)
    titulo_mas_largo = ""
    anio_publicacion = ""
    cantidad_caracteres = 0
    for linea in lista_lineas_1:
            titulo = str(linea[65:]).strip().strip('\t')
            año = str(linea[:4])
            if len(titulo) > cantidad_caracteres:
                cantidad_caracteres = len(titulo)
                anio_publicacion = año
                titulo_mas_largo = titulo
    return titulo_mas_largo, cantidad_caracteres, anio_publicacion
 
titulo_largo = titulo_original_largo(archivo_leido)
#print(titulo_largo)


#Título original mas corto (en cantidad de carácteres) y su año de publicación.
def titulo_original_corto(archivo_leido):
    lista_lineas_1 = lista_lineas(archivo_leido)
    titulo_mas_corto = ""
    anio_publicacion = ""
    cantidad_caracteres = 100
    for linea in lista_lineas_1:
            titulo = str(linea[65:]).strip().strip('\t')
            año = str(linea[:4])
            if len(titulo) < cantidad_caracteres:
                cantidad_caracteres = len(titulo)
                anio_publicacion = año
                titulo_mas_corto = titulo
    return titulo_mas_corto, cantidad_caracteres, anio_publicacion
 
titulo_corto = titulo_original_corto(archivo_leido)
#print(titulo_corto)


#Lista ordenada alfabéticamente con las 10 palabras que mas se repiten. 
def palabras_mas_repetidas(archivo_leido):
    from collections import Counter
    lista_lineas_1 = lista_lineas(archivo_leido)
    lista_palabras = []
    for lineas in lista_lineas_1:
        lista_palabras.extend(lineas.split())
    contador = Counter(lista_palabras)
    diez_palabras_repetidas = []
    for x, y in contador.most_common(10):
        diez_palabras_repetidas.append(x)
    return sorted(diez_palabras_repetidas)
 
diez = palabras_mas_repetidas(archivo_leido) 
#print(diez)

def titulos_castellano(arhivo_leido):
    lista_lineas_1 = lista_lineas(archivo_leido)
    titulos_castellano_1 = []
    for linea in lista_lineas_1:
        titulos = linea[4:63].strip()
        titulos_castellano_1.append(titulos)
    return titulos_castellano_1

#print(titulos_castellano(archivo_leido))

def titulos_originales(arhivo_leido):
    lista_lineas_1 = lista_lineas(archivo_leido)
    titulos_originales_1 = []
    for linea in lista_lineas_1:
        titulos = linea[63:].strip()
        titulos_originales_1.append(titulos)
    return titulos_originales_1

#print(titulos_originales(archivo_leido))

#Cantidad promedio de palabras en los títulos originales.
def promedio_palabras_titulos_originales(archivo_leido):
    titulos_origianles_1 = titulos_originales(archivo_leido)
    cantidad_titulos = len(titulos_origianles_1)
    lista_palabras = []
    for x in titulos_origianles_1:
        palabra = x.split()
        lista_palabras.extend(palabra)
    cantidad_palabras = len(lista_palabras)
    promedio = cantidad_palabras/cantidad_titulos
    return f"{promedio:.2f}"

#print(promedio_palabras_titulos_originales(archivo_leido))

#Cantidad promedio de palabras en los títulos en castellano.
def promedio_palabras_titulos_castellano(archivo_leido):
    titulos_castellano_1 = titulos_castellano(archivo_leido)
    cantidad_titulos = len(titulos_castellano_1)
    lista_palabras = []
    for x in titulos_castellano_1:
        palabra = x.split()
        lista_palabras.extend(palabra)
    cantidad_palabras = len(lista_palabras)
    promedio = cantidad_palabras/cantidad_titulos
    return f"{promedio:.2f}"

#print(promedio_palabras_titulos_castellano(archivo_leido))

#Lista de títulos idénticos en un idioma y otro.
def titulos_identicos(archivo_leido):
    titulos_castellano_1 = titulos_castellano(archivo_leido)
    titulos_originales_1 = titulos_originales(archivo_leido)
    titulos_identicos = []
    for x in titulos_castellano_1:
        if x in titulos_originales_1:
            titulos_identicos.append(x)
    return titulos_identicos

#print(titulos_identicos(archivo_leido))

#Lista de títulos donde aparecen números.
def titulos_con_numeros(archivo_leido):
    titulos_castellano_1 = titulos_castellano(archivo_leido)
    titulos_originales_1 = titulos_originales(archivo_leido)
    titulos_con_numeros = []
    for titulo in titulos_castellano_1:
        if re.search('[0-9]', titulo):
            titulos_con_numeros.append(titulo)
    for titulo in titulos_originales_1:
        if re.search('[0-9]', titulo):
            titulos_con_numeros.append(titulo)
    return titulos_con_numeros

#print(titulos_con_numeros(archivo_leido))