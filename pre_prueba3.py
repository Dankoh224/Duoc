import time
import random
opcion_principal = True
while opcion_principal:
    print("************************************")
    print("*         MENÚ PRINCIPAL           *")
    print("************************************")
    print("1.	Grabar                        *")
    print("2.	Buscar                        *") 
    print("3.	Imprimir                      *") 
    print("4.	Salir                         *")
    print("************************************")
    opcion_principal = str(input("Ingrese el número de la opción que desea elegir: "))

# Bloque 1: Opción de registro del cliente.
# Se refiere a guardar:
# Número de Parte (Validar número de parte. Puede crear varios, mínimo 10).
# Nombre del producto (6 caracteres mínimo).
# Precio del producto (Precio mayor a cero).

    if opcion_principal == "1":
        letras = "abcdefghijklmnopqrstuvwxyz"
        numero_final = ""
        for i in range(6):
            numero = random.randint(0,9)
            numero_final = numero_final + str(numero)
        
        l = random.randint(0,25)
        letra_al_azar = letras[l]
        numero_final = numero_final + "-" + letra_al_azar.upper()
        print(numero_final)

        for i in range(2):
            secuencia_dos_numeros = ""
            numero = random.randint(0,9)
            numero_final = numero_final + str(numero)
        print(numero_final)        




# Bloque 2: Opción de atencion al cliente.

    elif opcion_principal == "2":
        print("¡Haz elegido Atención Cliente!")
        verificacionRun = str(input("Ingrese su run para verificar si se encuentra registrado en el sistema: "))
        if verificacionRun in listaRun:
            posicionRun = listaRun.index(verificacionRun)
            fechaAtencion = str(input("Ingrese la fecha de hoy. Use el formato dia/mes/año: "))
            observacion = str(input("Ingrese las observaciones: "))

            listaRegistro.insert(posicionRun,"Fecha {}. Observaciones: {}".format(fechaAtencion,observacion))
            del listaRegistro[posicionRun+1]
            print("Todo Ok ¡Ingreso exitoso!")
        else:

            print("Las anotaciones no se llevaron a cabo. Para ingresar anotaciones debe registrarse previamente")
        
        # Opción principal lograda. Ahora a salir del programa o a seguir utilizandolo:

        print("¿Quieres salir del programa?")
        salir = str(input('Ingresa "s" si quieres salir del programa o "n" si quieres volver al menu principal: '))
        salir = salir.lower()
        if salir == "s":
            print("Has elegido salir del programa. Gracias por confiar en nosotros.¡Hasta pronto!")
            opcion_principal = False
        elif salir == "n":
            print("¡Elegiste volver al MENÚ PRINCIPAL!")
        else:
            salir = str(input("¡Opción incorrecta! Vuelve a intentarlo: "))

# Bloque 3: Opción de consulta datos cliente.


    elif opcion_principal == "3":
        print("¡Haz elegido Consultar Datos Cliente!")
        consulta = str(input("Ingrese el run del cliente para conocer sus datos asociados: "))
        print()
        if consulta in listaRun:
            posicionConsulta = listaRun.index(consulta)
            print("Nombre y apellido: {} {}".format(listaNombre[posicionConsulta],listaApellido[posicionConsulta]))
            print("Rut: {}".format(listaRun[posicionConsulta]))
            print("Dirección: {}".format(listaDireccion[posicionConsulta]))
            print("Correo: {}".format(listaCorreo[posicionConsulta]))
            print("Edad: {}".format(listaEdad[posicionConsulta]))
            print("Género: {}".format(listaGenero[posicionConsulta]))
            print("Registro: {}".format(listaRegistro[posicionConsulta]))
            print("PS: {}".format(listaPS[posicionConsulta]))

        else:
            print("El run ingresado no se encuentra registrado en nuestro sistema.")

        # Opción principal lograda. Ahora a salir del programa o a seguir utilizandolo:

        print("¿Quieres salir del programa?")
        salir = str(input('Ingresa "s" si quieres salir del programa o "n" si quieres volver al menu principal: '))
        salir = salir.lower() 
        if salir == "s":
            print("Has elegido salir del programa. Gracias por confiar en nosotros.¡Hasta pronto!")
            opcion_principal = False
        elif salir == "n":
            print("¡Elegiste volver al MENÚ PRINCIPAL!")
        else:
            salir = str(input("¡Opción incorrecta! Vuelve a intentarlo: "))

# Bloque 4: Finalizar programa.

    elif opcion_principal == "4":
        print("¿Seguro que quieres salir del programa?")
        salir = str(input('Ingresa "s" si quieres salir del programa o "n" si quieres volver al menu principal: '))
        salir = salir.lower()
        if salir == "s":
            print("Has elegido salir del programa. Gracias por confiar en nosotros.¡Hasta pronto!")
            opcion_principal = False
        elif salir == "n":
            print("¡Elegiste volver al MENÚ PRINCIPAL!")
        else:
            salir = str(input("¡Opción incorrecta! Vuelve a intentarlo: "))
    
    else:
        print("¡No haz elegido una opción correcta! ¡Vuelve a intentarlo!")