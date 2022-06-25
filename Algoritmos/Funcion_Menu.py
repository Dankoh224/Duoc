import numpy as np
import random

rut = []
nombre = []
apellido = []
edad = []
estado_civil = []
genero = []
fecha_afiliacion = []

while True:
    print('1.- Grabar')
    print('2.- Buscar')
    print('3.- Imprimir certificados')
    print('4.- Salir')
    opcion = int(input("Ingrese la opción que desea: "))

    if opcion == 1:
        rut_persona = int(input("Ingrese su rut: "))
        rut.append(rut_persona)
        nombre_persona = str(input("Ingrese su nombre: "))
        nombre.append(nombre_persona)
        apellido_persona = str(input("Ingrese apellido: "))
        apellido.append(apellido_persona)
        while True:
            edad_persona = int(input("Ingrese su edad: "))
            if edad_persona >= 18:
                break
            else:
                print("La edad ingresada debe ser de 18 años o mayor.")
        edad.append(edad_persona)
        while True:
            estado_civil_persona = str(input("Ingrese su estado civil(C = Casado, S = Soltero, V = Viudo): "))
            estado_civil_persona = estado_civil_persona.lower()
            if estado_civil_persona == "c" or estado_civil_persona == "s" or estado_civil_persona == "v":
                break
            else:
                print("La opción ingresada no es válida.")
        estado_civil.append(estado_civil_persona)
        genero_persona = str(input("Ingrese su género: "))
        genero.append(genero_persona)
        fecha_afiliacion_persona = str(input("Ingrese la fecha de afiliación: "))
        fecha_afiliacion.append(fecha_afiliacion_persona)

    if opcion == 2:
        buscar_rut = int(input("Ingrese el rut a buscar: "))
        if buscar_rut in rut:
            posicion = rut.index(buscar_rut)
            print("Rut: ",rut[posicion])
            print("Nombre: ",nombre[posicion])
            print("Apellido: ",apellido[posicion])
            print("Edad: ", edad[posicion])
            print("Estado Civil: ",estado_civil[posicion])
            print("Género: ", genero[posicion])
            print("Fecha Afiliación: ",fecha_afiliacion[posicion])
        else:
            print("No está")

    if opcion == 3:
        buscar_rut = int(input("Ingrese el rut para generar el certificado: "))
        if buscar_rut in rut:
            print()
            print("******** Certificado de afiliación ********")
            print("Número de Certificado: {}".format(random.randint(1000,1500)))
            posicion = rut.index(buscar_rut)
            print("Rut: ",rut[posicion])
            print("Nombre: ",nombre[posicion])
            print("Apellido: ",apellido[posicion])
            print("Edad: ", edad[posicion])
            print("Estado Civil: ",estado_civil[posicion])
            print("Género: ", genero[posicion])
            print("Fecha Afiliación: ",fecha_afiliacion[posicion])
        else:
            print("No está el rut especificado.")

    if opcion == 4:
        print("Ha decidido salir. Creador del programa: Danko Valderrama. Versión del programa: 2.2.")
        break

    else:
        print()
