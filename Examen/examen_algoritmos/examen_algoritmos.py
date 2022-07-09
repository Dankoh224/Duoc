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
    opcion = str(input("Ingrese opción: "))
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

# Cantidad de ventas:
depto_A = []
depto_B = []
depto_C = []
depto_D = []

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
    while True:
        piso = str(input("Ingrese el PISO donde comprará su departamento: "))
        if piso in ["1","2","3","4","5","6","7","8","9","10"]:
            piso = int(piso)
            break
        else:
            print("La opción ingresada es incorrecta, vuelva a intentarlo.")
    while True:
        tipo = str(input("Ingrese el TIPO de departamento que comprará: "))
        tipo = tipo.upper()
        if tipo in ["A","B","C","D"]:
            break
        else:
            print("La opción ingresada es incorrecta, vuelva a intentarlo.")

    # Conteo departamentos:
    if tipo == "A":
        depto_A.append(1)
    elif tipo == "B":
        depto_B.append(1)
    elif tipo == "C":
        depto_C.append(1)
    elif tipo == "D":
        depto_D.append(1)

    # Continuación:
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
    print("| {:<9}{:<9}{:<9} |".format("Rut","Nombre","Depto"))
    for i in datos_ordenados:
        print("|", end = " ") 
        for elemento in i:
            print("{:<9}".format(elemento), end = "") 
        print(" |")
    print()
    return datos_ordenados

# Función opción 4:
def ventas_totales():
    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0

    # Lista de ventas:
    ventas = [ 
        ["Tipo Depto","Cantidad","Total"],
        ["Tipo A 3.800 UF",sum(depto_A),sum(depto_A) * 3800],
        ["Tipo B 3.000 UF",sum(depto_B),sum(depto_B) * 3000], 
        ["Tipo C 2.800 UF",sum(depto_C),sum(depto_C) * 2800],   
        ["Tipo D 3.500 UF",sum(depto_D),sum(depto_D) * 3500],
        ["Total",sum(depto_A) + sum(depto_B) + sum(depto_C) + sum(depto_D),sum(depto_A) * 3800 + sum(depto_B) * 3000 + sum(depto_C) * 2800 + sum(depto_D) * 3500]
    ]
    print()
    for i in ventas:
        print("|", end = "") 
        for elemento in i:
            print("{:16}".format(elemento), end = " ") 
        print("|")
    print()


bandera = True
while bandera:
    opcion = menu()
    if opcion == "1":
        compra_departamento = comprar_departamento()
    elif opcion == "2":
        muestra_depto = mostrar_departamentos_disponibles()
    elif opcion == "3":
        ver = listado_compradores()
    elif opcion == "4":
        ganancias_totales = ventas_totales()
    elif opcion == "5":
        print("Ha elegido salir. Programa realizado por Danko Valderrama. Fecha: 8 de julio 2022.")
        bandera = False
    else:
        print("Opción equivocada. Vuelva a intentarlo. ")
