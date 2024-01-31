from biblioteca import *
import os

presentacion()

while True:
    opcion = input("           Ingrese una opción: ")
    print()
    os.system('clear')
    print(presentacion())
    os.system('clear')
    if opcion == '1':
            resultado = rango_años(archivo_leido)
            print (f"    El autor publicó obras entre {resultado[0]} y {resultado[1]}")
            print()
    elif opcion == '2':
        resultado = anio_sin_obras(archivo_leido)
        print (f"    El autor no publicó obras en:", str(resultado) [1:-1])
        print()
    elif opcion == '3':
        resultado = anio_mas_obras(archivo_leido)
        print (f"    El autor publicó más obras en: {resultado}")
        print()
    elif opcion == '4':
        resultado = titulo_original_largo(archivo_leido)
        print (f"    El titulo original más largo es: {resultado[0]}, tiene {resultado[1]} caracteres y se publicó en {resultado[2]}")
        print()
    elif opcion == '5':
        resultado = titulo_original_corto(archivo_leido)
        print (f"    El titulo original más corto es: {resultado[0]}, tiene {resultado[1]} caracteres y se publicó en {resultado[2]}")
        print()
    elif opcion == '6':
        resultado = titulos_castellano_largo(archivo_leido)
        print (f"   El titulo en castellano más largo es: {resultado[0]}, tiene {resultado[1]} caracteres y se publicó en {resultado[2]}")
        print( )
    elif opcion == '7':
        resultado = titulo_castellano_corto(archivo_leido)
        print (f"    El titulo en castellano más corto es: {resultado[0]}, tiene {resultado[1]} caracteres y se publicó en {resultado[2]}")
        print()
    elif opcion == '8':
        resultado = palabras_mas_repetidas(archivo_leido)
        print (f"    Las diez palabras más repetidas son:", *resultado, sep= ',')
        print()
    elif opcion == '9':
        resultado = promedio_palabras_titulos_originales(archivo_leido)
        print (f"    El promedio de palabras en los títulos originales es: {resultado}")
        print()
    elif opcion == '10':
        resultado = promedio_palabras_titulos_castellano(archivo_leido)
        print (f"    El promedio de palabras en los títulos en castellano es: {resultado}")
        print()
    elif opcion == '11':
        resultado = titulos_identicos(archivo_leido)
        print (f"    Títulos idénticos en ambos idiomas:")
        for x in resultado:
            print("     ",str(x))
        print()
    elif opcion == '12':
        resultado = titulos_con_numeros(archivo_leido)
        print (f"   Títulos donde aparecen números:")
        for x in resultado:
            print("     ",str(x))
        print( )
    elif opcion == '13':
        print()
        print (f"       GRACIAS POR USAR  EL PROGRAMA       ")
        print()
        break
    else:
        print("    Opción inválida, intente nuevamente")
        print()