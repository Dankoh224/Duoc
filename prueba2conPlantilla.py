import time
print("¡Hola! Bienvenido al Centro medico Duoc")
opcion_principal = True
listaRun = []
listaNombre = []
listaApellido = []
listaDireccion = []
listaCorreo = []
listaEdad = []
listaGenero = []
listaRegistro = []
listaPS = []

listaDatosPaciente = [
    listaRun,
    listaNombre,
    listaApellido,
    listaDireccion,
    listaCorreo,
    listaEdad,
    listaGenero,
    listaRegistro,
    listaPS
    ]

listaDatosPaciente = []

while opcion_principal:
    print("************************************")
    print("*         MENÚ PRINCIPAL           *")
    print("************************************")
    print("1.	Registrar paciente          *")
    print("2.	Atención al paciente               *") 
    print("3.	Consultar Datos paciente    *") 
    print("4.	Salir                      *")
    print("************************************")
    opcion_principal = str(input("Ingrese el número de la opción que desea elegir: "))

# Bloque 1: Opción de registro del cliente.
# Cada vez que se registre un cliente, deben ingresarse sus datos en una lista.

    if opcion_principal == "1":
        print("¡Haz elegido Registrarte! Solo te pediremos unos datos.")
        run = True
        while run:
            run = str(input("Ingresa tu run SIN digito verificador y sin puntos: "))
            if int(run) > 5000000 and int(run) < 99999999:
                print("El run fue registrado correctamente.")
                listaRun.append(run)
                run = False
            else:
                print("El run ingresado no es válido.")
                print("Vuelva a intentar.")
                run = True      
        
        nombre = True
        while nombre:
            nombre = str(input("Ingresa tu primer nombre: "))
            if len(nombre) != 0:
                print("El nombre fue registrado correctamente.")
                listaNombre.append(nombre)
                nombre = False
            else:
                print("Ingresar su nombre en el campo, es obligatorio.")
                print("Vuelva a intentar.")
                nombre = True   
        apellido = True
        while apellido:
            apellido = str(input("Ingresa tu primer apellido: "))
            if len(apellido) != 0:
                print("El apellido fue registrado correctamente.")
                listaApellido.append(apellido)
                apellido = False
            else:
                print("Ingresar su apellido en el campo, es obligatorio.")
                print("Vuelva a intentar.")
                apellido = True    
        direccion = True
        while direccion:
            direccion = str(input("Ingresa la ciudad donde vives: "))
            if len(direccion) != 0:
                print("La ciudad fue registrada correctamente.")
                listaDireccion.append(direccion)
                direccion = False
            else:
                print("Ingresar su ciudad en el campo, es obligatorio.")
                print("Vuelva a intentar.")
                direccion = True 
        correo = True
        while correo:
            correo = str(input("Ingresa tu correo: "))
            if "@" in correo:
                print("Su correo fue registrado correctamente.")
                listaCorreo.append(correo)
                correo = False 
            else:
                print("El correo ingresado no es válido.")
                print("Vuelva a ingresarlo.")
                correo = True
        edad = True
        while edad:
            edad = str(input("Ingresa tu edad: "))
            if int(edad) >= 0 and int(edad) <= 110:
                print("Su edad fue registrada correctamente.")
                listaEdad.append(edad)
                edad = False
            else:
                print("La edad ingresada no es válida.")
                print("Vuelva a ingresarla.")
                edad = True

        genero = True
        while genero:
            genero = str(input('¿Cuál es tu género? Ingresa "m" si eres mujer o una "h" si eres hombre: '))
            if genero == "m" or genero == "h":
                print("El género fue registrado correctamente.")
                if genero == "m":
                    listaGenero.append("mujer")
                if genero == "h":
                    listaGenero.append("hombre")
                genero = False
            else:
                print("El género ingresado no es correcto.")
                print("Vuelva a ingresarlo.")
                genero = True

        listaRegistro.append("Vacío")

        PS = True
        while PS:
            PS = str(input('¿Cuál es tu género? Ingresa "m" si eres mujer o una "h" si eres hombre: '))
            if PS == "m" or PS == "h":
    
                print("El género fue registrado correctamente.")
                if PS == "m":
                    listaPS.append("mujer")
                if PS == "h":
                    listaPS.append("hombre")
                PS = False
            else:
                print("El género ingresado no es correcto.")
                print("Vuelva a ingresarlo.")
                PS = True
        print("¡REGISTRO EXITOSO!")

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