lista_rut = []
lista_nombre = []
lista_apellido = []
lista_direccion = []
lista_correo = []
lista_edad = []
lista_sexo = []
lista_registro = []
lista_PS = []

banderin = True
while banderin:
    print("MENU")
    print("1. Registrar paciente")
    print("2. Atencion Paciente")
    print("3. Consultar Datos Paciente")
    print("4. Salir")
    try:
        opcion_principal = int(input("Ingrese la opción: "))
        if opcion_principal == 1:
            print("Registre los datos del paciente:")
            bandera = True
            while bandera:
                rut = int(input("Ingrese rut sin dígito verificador ni puntos: "))
                if rut >= 5000000 and rut <= 99999999:
                    bandera = False
                else:
                    print("El rut es incorrecto. Vuelva a intentar.")
                    bandera = True
            nombre = str(input("Ingrese su primer nombre: ")) 
            apellido = str(input("Ingrese apellido paterno: ")) 
            dirección = str(input("Ingrese su dirección: "))
            bandera = True
            while bandera:
                correo =  str(input("Ingrese su correo: "))
                if "@" in correo:
                    bandera = False
                else:
                    print("El correo es incorrecto. Vuelva a intentar.")
                    bandera = True
            bandera = True
            while bandera:
                try:
                    edad =  int(input("Ingrese su edad: "))
                    if edad >= 0 and edad <= 110:
                        bandera = False
                    else:
                        print("La edad es incorrecta. Vuelva a intentar.")
                        bandera = True
                except:
                    print("La edad no admite letras.")
            bandera = True
            while bandera:
                sexo = str(input('Ingrese su sexo. "F" si es femenino o "M" si es masculino: '))
                sexo.lower()
                if sexo == "f" or sexo == "m":
                    bandera = False
                else:
                    print("El sexo es incorrecto. Vuelva a intentar.")
                    bandera = True
            bandera = True
            while bandera:
                PS = str(input('Ingrese la letra "F" si pertenece a FONASA o ingrese la letra "I" si pertenece a ISAPRE: '))
                PS.lower()
                if PS == "f" or PS == "i":
                    bandera = False
                else:
                    print("El tipo de salud es incorrecto. Vuelva a intentar.")
                    bandera = True

# -----------------------------------------LISTAS ----------------------------------------------          
            lista_rut.append(rut)
            lista_nombre.append(nombre)
            lista_apellido.append(apellido)
            lista_direccion.append(dirección)
            lista_correo.append(correo)
            lista_edad.append(edad)
            lista_sexo.append(sexo)
            lista_PS.append(PS)

            lista_datos_paciente = [
                lista_rut,
                lista_nombre,
                lista_apellido,
                lista_direccion,
                lista_correo,
                lista_edad,
                lista_sexo,
                lista_registro,
                lista_PS
            ]

            print(lista_datos_paciente)

        elif opcion_principal == 2:
            try:
                rut_paciente = int(input("Ingrese rut del paciente: "))
                if rut_paciente in lista_rut:
                    posicion_rut = lista_rut.index(rut_paciente)
                    print(posicion_rut)
                    print("El paciente esta en nuestros registros.")
                    fecha = str(input("Ingrese la fecha de atención: "))
                    observacion = str(input("Ingrese las observaciones de la atención: "))
                    registro = "fecha: {}. Observaciones: {}".format(fecha,observacion)
                    print(registro)
                    lista_registro.insert(posicion_rut,registro)
                else:
                    print("El paciente NO está en nuestros registros.")
            except:
                print("Debe ingresar el rut usando solo números")
        elif opcion_principal == 3:
            try:
                rut_paciente = int(input("Ingrese rut del paciente: "))
                if rut_paciente in lista_rut:
                    posicion_rut = lista_rut.index(rut_paciente)
                    print("El paciente esta en nuestros registros.")
                    print("Datos del paciente:")
                    print("Rut: {}".format(lista_rut[posicion_rut]))
                    print("Nombre: {}".format(lista_nombre[posicion_rut]))
                    print("apellido: {}".format(lista_apellido[posicion_rut]))
                    print("direccion: {}".format(lista_direccion[posicion_rut]))
                    print("correo: {}".format(lista_correo[posicion_rut]))
                    print("edad: {}".format(lista_edad[posicion_rut]))
                    print("sexo: {}".format(lista_sexo[posicion_rut]))
                    print("registro: {}".format(lista_registro[posicion_rut]))
                    print("PS: {}".format(lista_PS[posicion_rut]))                    
                else:
                    print("El paciente NO está en nuestros registros.")
            except:
                print("Debe ingresar el rut usando solo números")
            print()
        elif opcion_principal == 4:
            print("Usted a ingresado la opcion para salir del sistema")
            banderin = False
        else:
            print("Opción inexistente. Vuelva a intentar.")
    except ValueError:
        print("Ingreso mal el dato")