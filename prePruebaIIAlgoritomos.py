print("Bienvenido a Juan Maestro App")
opcion_principal = True
listaRun = []
listaNombre = []
listaApellido = []
listaCiudad = []
listaComuna = []
listaCalle = []
listaNumero = []
listaBlock = []
listaNumDepartamento = []
listaCorreo = []
listaEdad = []
listaGenero = []
listaCelular = []
listaTipo = []
listaSuscripcion = []

listaCliente = [
    listaRun,
    listaNombre,
    listaApellido,
    listaCiudad,
    listaComuna,
    listaCalle,
    listaNumero,
    listaBlock,
    listaNumDepartamento,
    listaCorreo,
    listaEdad,
    listaGenero,
    listaCelular,
    listaTipo,
    listaSuscripcion]

listaClienteSuscrito = [

]

while opcion_principal:
    print("************************************")
    print("*         MENÚ PRINCIPAL           *")
    print("************************************")
    print("1.	Registrar Cliente          *")
    print("2.	Suscripción                *") 
    print("3.	Consultar Datos Cliente    *") 
    print("4.	Salir                      *")
    print("************************************")
    opcion_principal = str(input("Ingrese el número de la opción que desea: "))

# Bloque 1: Opción de registro del cliente.
# Cada vez que se registre un cliente, deben ingresarse sus datos en una lista.

    if opcion_principal == "1":
        print("¡Haz elegido Registrarte! Solo te pediremos unos datos.")

        run = True
        while run:
            run = str(input("Ingresa tu run SIN digito verificador y sin puntos: "))
            if int(run) > 4000000 and int(run) < 99999999:
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

        ciudad = True
        while ciudad:
            ciudad = str(input("Ingresa la ciudad donde vives: "))
            if len(ciudad) != 0:
                print("La ciudad fue registrada correctamente.")
                listaCiudad.append(ciudad)

                ciudad = False
            else:
                print("Ingresar su ciudad en el campo, es obligatorio.")
                print("Vuelva a intentar.")
                ciudad = True 
        
        comuna = True
        while comuna:
            comuna = str(input("Ingresa tu comuna: "))
            if len(comuna) != 0:
                print("La comuna fue registrada correctamente.")
                listaComuna.append(comuna)
                comuna = False
            else:
                print("Ingresar su comuna en el campo, es obligatorio.")
                print("Vuelva a intentar.")
                comuna = True 

        calle = True
        while calle:
            calle = str(input("Ingresa tu calle: "))
            if len(calle) != 0:
                print("La calle fue registrada correctamente.")
                listaCalle.append(calle)
                calle = False
            else:
                print("Ingresar su calle en el campo, es obligatorio.")
                print("Vuelva a intentar.")
                calle = True 

        numero = True
        while numero:
            numero = str(input("Ingresa el número del lugar donde vives: "))
            if len(numero) != 0:
                print("El número fue registrado correctamente.")
                listaNumero.append(numero)
                numero = False
            else:
                print("Ingresar su número de dirección en el campo, es obligatorio.")
                print("Vuelva a intentar.")
                numero = True 

        block = str(input("Ingresa el número del block o edificio: En caso contrario, solo presiona enter: "))
        if len(block) == 0:
            print("Se registró correctamente que usted no vive en block.")
            listaBlock.append("No aplica.")
        else:
            print("El número del block fue registrado correctamente.")
            listaBlock.append(block)
            numeroDepartamento = True 

        numeroDepartamento = True
        if block != "":
            while numeroDepartamento:
                numeroDepartamento = str(input("Ingresa el número de tu departamento: "))
                if len(numeroDepartamento) != 0:
                    print("El número del departamento fue registrado correctamente.")
                    listaNumDepartamento.append(numeroDepartamento)
                    numeroDepartamento = False
                else:
                    print("Ingresar su número de departamento en el campo, es obligatorio.")
                    print("Vuelva a intentar.")
                    numeroDepartamento = True
        else:
            listaNumDepartamento.append("No aplica.")

        correo = True
        while correo:
            correo = str(input("Ingresa tu correo: "))
            if (".cl" == correo[len(correo)-3] + correo[len(correo)-2] + correo[len(correo)-1] or ".com" == correo[len(correo)-4] + correo[len(correo)-3] + correo[len(correo)-2] + correo[len(correo)-1] or ".org" == correo[len(correo)-4] + correo[len(correo)-3] + correo[len(correo)-2] + correo[len(correo)-1]) and "@" in correo:
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

        celular = True
        while celular:
            celular = str(input("Ingresa tu celular: +569"))
            if len(celular) == 8:
                print("El número celular fue registrado correctamente.")
                listaCelular.append("+569{}".format(celular))
                celular = False
            else:
                print("Ingresar un número de celular válido.")
                print("Vuelva a intentar.")
                celular = True 

        suscripcion = "Suscrito"
        listaSuscripcion.append(suscripcion)
        
        tipo = True
        while tipo:
            tipo = str(input("Ingresa el nombre de la suscripción que deseas (PREMIUM, GOLD o SILVER): "))
            tipo.lower()
            if tipo == "premium" or tipo == "gold" or tipo == "silver":
                suscripcionElegida = tipo
                print("El tipo de suscripción fue registrada correctamente.")
                listaTipo.append(tipo)
                tipo = False
            else:
                print("El tipo de suscripción ingresado es incorrecto.")
                print("Vuelva a ingresarlo.")
                tipo = True
        

        
        print("¡Registro Exitoso!")

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

# Bloque 2: Opción de suscripción del cliente.

    elif opcion_principal == "2":
        print("¡Haz elegido Suscribirte!")
        verificacionRun = str(input("Ingrese su run para verificar si se encuentra registrado en el sistema: "))
        if verificacionRun in listaRun:
            fechaSuscripcion = str(input("Ingrese la fecha de hoy. Use el formato dia/mes/año: "))
            listaClienteSuscrito.append("Cliente: {}. Fecha Suscripción: {}".format(verificacionRun,fechaSuscripcion))
            print("Todo Ok ¡Suscripción Exitosa!")
        else:
            print("La suscripción no se llevo a cabo. Para suscribirse debe registrarse previamente")
        
        print(listaClienteSuscrito)
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
        if consulta in listaRun:
            posicionConsulta = listaRun.index(consulta)
            print("Nombre y apellido: {} {}".format(listaNombre[posicionConsulta],listaApellido[posicionConsulta]))
            print("Rut: {}".format(listaRun[posicionConsulta]))
            print("Dirección: calle {} #{}, {}, {}. Block: {}. Departamento: {}".format(listaCalle[posicionConsulta],listaNumero[posicionConsulta],listaComuna[posicionConsulta],listaCiudad[posicionConsulta],listaBlock[posicionConsulta],listaNumDepartamento[posicionConsulta]))
            print("Correo: {}".format(listaCorreo[posicionConsulta]))
            print("Edad: {}".format(listaEdad[posicionConsulta]))
            print("Género: {}".format(listaGenero[posicionConsulta]))
            print("Celular: {}".format(listaCelular[posicionConsulta]))
            print("Estado suscripción: {}".format(listaSuscripcion[posicionConsulta]))
            print("Tipo de suscripción: {}".format(listaTipo[posicionConsulta]))

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