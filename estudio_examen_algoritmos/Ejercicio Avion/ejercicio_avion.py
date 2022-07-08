import numpy as np 

def menu():
    print("1. Ver asientos disponibles")
    print("2. Comprar asiento")
    print("3. Anular vuelo")
    print("4. Modificar datos de pasajero")
    print("5. Salir")
    opcion = int(input("Ingrese opción: "))
    return opcion

def asientos_disponibles ():
    print("-------- Asientos Disponibles -------")
    asientos_disponibles = [
    [1,2,3,4,5,6],
    [7,8,9,10,11,12],
    [13,14,15,16,17,18],
    [19,20,21,22,23,24],
    [25,26,27,28,29,30],
    ["  ____________","       ____________"],
    ["  ____________","       ____________"],
    [31,32,33,34,35,36],
    [37,38,39,40,41,42]
    ]
    for i in asientos_disponibles: 
        print("|", end = "") 
        for elemento in i:
            if i.index(elemento) == 2:
                print("{:4}".format(elemento), end = "      ") 
            else:
                print("{:4}".format(elemento), end = " ") 
        print("|")
        
def comprar_asiento ():
    print("Formulario Datos Cliente.")
    nombre_pasajero = str(input("Ingrese su nombre completo: "))
    rut = int(input("Ingrese su rut: "))
	telefono = int(input("Ingrese su número de telefono: "))
    nombre_banco = str(input("Ingrese el nombre del banco: "))