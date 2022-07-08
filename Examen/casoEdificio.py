import copy

# función menú:
def menu ():
    print("-------------------------------------")
    print("                MENU                 ")
    print("-------------------------------------")
    print("1. Comprar departamento.")
    print("2. Mostrar departamentos disponibles.")
    print("3. Ver listado de compradores.")
    print("4. Mostrar ganancias totales.")
    print("5. Salir.")
    print("-------------------------------------")
    opcion = int(input("Ingrese opción: "))
    return opcion

# Lista departamentos:
departamentos = [ 
    ["PISO","Tipo               "],
    ["","A","B","C","D"],
    ["10","","","",""],
    ["9","","","",""],
    ["8","","","",""], 
    ["7","","","",""],   
    ["6","","","",""],
    ["5","","","",""],
    ["4","","","",""],
    ["3","","","",""],
    ["2","","","",""],
    ["1","","","",""]
]

# Listas de datos:
ruts = []
nombres = []
deptos = []
datos_ordenados = []

# Función opción 1:
def comprar_departamento():
    print()
    print("|Departamentos Disponibles|")
    for i in departamentos:
        print("|", end = "") 
        for elemento in i:
            print("{:4}".format(elemento), end = " ") 
        print("|")
    print()
    print("Estimado cliente ¿Cuál es el departamento a comprar? Existen 10 pisos a elegir y 4 tipos de departamentos por piso:")
    print()
    print("Tipo A, 3.800 UF")
    print("Tipo B, 3.000 UF")
    print("Tipo C, 2.800 UF")
    print("Tipo D, 3.500 UF")
    print()
    piso = int(input("Ingrese el PISO donde comprará su departamento: "))
    tipo = str(input("Ingrese el TIPO de departamento que comprará: "))
    tipo = tipo.upper()
    posicion_tipo = departamentos[1].index(tipo)
    numero_departamento = tipo + str(piso)
    if departamentos[12-piso][posicion_tipo] == "":
        departamentos[12-piso][posicion_tipo] = "X"
        run = int(input("Ingrese el run del comprador, sin puntos y sin digito verificador: "))
        ruts.append(run)
        nombre_completo = str(input("Ingrese nombre completo de quién compra: "))
        nombres.append(nombre_completo)
        deptos.append(numero_departamento)
        print()
        print("La operación se ha realizado correctamente.")
    else:
        print("Este departamento NO está disponible. Debe seleccionar otro.")
    return numero_departamento

# Función opción 2:
def mostrar_departamentos_disponibles():
    print()
    print("|Departamentos Disponibles|")
    for i in departamentos:
        print("|", end = "") 
        for elemento in i:
            print("{:4}".format(elemento), end = " ") 
        print("|")
    print()

# Función opción 3:
def  listado_compradores():
    del datos_ordenados[:]
    ruts_copia = copy.deepcopy(ruts)
    nombres_copia = copy.deepcopy(nombres)
    deptos_copia = copy.deepcopy(deptos)
    for i in range(len(ruts_copia)):
        rut_menor = min(ruts_copia)
        posicion_rut_menor = ruts_copia.index(rut_menor)
        datos_ordenados.append([rut_menor,nombres_copia[posicion_rut_menor],deptos_copia[posicion_rut_menor]])
        del ruts_copia[posicion_rut_menor]
        del nombres_copia[posicion_rut_menor]
        del deptos_copia[posicion_rut_menor]
    return datos_ordenados



bandera = True
while bandera:
    opcion = menu()
    if opcion == 1:
        numero_departamento = comprar_departamento()
    elif opcion == 2:
        muestra_depto = mostrar_departamentos_disponibles()
    elif opcion == 3:
        ver = listado_compradores()
        print("| {:<9}{:<9}{:<9} |".format("Rut","Nombre","Depto"))
        for i in ver:
            print("|", end = " ") 
            for elemento in i:
                print("{:<9}".format(elemento), end = "") 
            print(" |")
        print()
    elif opcion == 4:
        print("4")
    elif opcion == 5:
        print("Ha elegido salir")
        bandera = False
    else:
        print("Opción equivocada. Vuelva a intentarlo. ")
