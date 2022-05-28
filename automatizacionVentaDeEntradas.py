# En un estadio, se requiere un programa para automatizar la venta de entradas a los clientes que van llegando al partido, según el tipo de cliente. Las tarifas son las siguientes:

# Menores: Mayores de 7 años y menores que 12; $4.000
# Adulto: Desde los 12 años hasta los 65; $7.000
# Adulto Mayor: Desde los 65 años; $3.000

# Desarrolle un programa en Python, que permita ingresar una compra o bien salir para terminar el día.

# Compras Boletos: opcion 1
# Salir: opcion 2

# Al ingresar una compra se debe determinar el total a pagar por un grupo de personas que llegan juntas al lugar. Por ejemplo, un grupo de 3 personas está compuesto por un menor, un adulto y un adulto mayor. Este grupo paga un total de $14.000.

# Se debe mostrar la siguiente información de salida:
# Compra
# 1 Menor(s): $4.000
# 1 Adulto(s): $7.000
# 1 Adulto Mayor(s): $3.000
# Total: $14000

# Al termino de cada día, nos tiene que entregar el total de personas que ingresa al estadio y el total acumulado en ventas. Se deben validar que las cantidades no sean números negativos ni letras y que sean valores en los rangos definidos.
import time
totalPersonas = 0
totalVentas = 0

while True:
    print("****************************")
    print("****************************")
    print("******     MENU     ********")
    print("****************************")
    print("****************************")
    print()
    print("Ingrese 1 si quiere ingresar una venta.")
    print("Ingrese 2 si quiere salir.")
    print()
    try:
        opcion = int(input("Ingrese aquí su opción:  "))
        if opcion == 1:
            print("¡Usted eligió ingresar una venta!")
            time.sleep(1)
            try:
                cantidadMenor = int(input("Cantidad de menores: "))
                cantidadAdulto = int(input("Cantidad de adultos: "))
                cantidadAdultoMayor = int(input("Cantidad de adultos mayores: "))
                precioMenor = cantidadMenor * 4000
                precioAdulto = cantidadAdulto * 7000
                precioAdultoMayor = cantidadAdultoMayor * 3000
                print()
                print("Compra")
                time.sleep(1)
                print("---------------------------")
                print("{} Menor(es):         ${:6}".format(cantidadMenor,precioMenor))
                print("{} Adulto(s):         ${:6}".format(cantidadAdulto,precioAdulto))
                print("{} Adulto Mayor(es):  ${:6}".format(cantidadAdultoMayor,precioAdultoMayor))
                print("---------------------------")
                print("Total: {:5}".format(precioMenor+precioAdulto+precioAdultoMayor))
                totalPersonas += cantidadMenor + cantidadAdulto + cantidadAdultoMayor
                totalVentas += precioMenor + precioAdulto + precioAdultoMayor
                print()
                enter = str(input('Presione "enter" para continuar: '))
                print()
            except ValueError:
                print()
                print("ERROR: La cantidad debe ingresarse con valores numéricos.")
                time.sleep(2)
        elif opcion == 2:
            print()
            print("¡Usted eligió salir del programa!")
            time.sleep(1)
            print("A continuación, el total de ventas y personas dentro del estadio:")
            print("Personas:         {:5}".format(totalPersonas))
            print("Venta total: ${:9}".format(totalVentas))
            print()
            break
        else:
            print("¡OPCION INCORRECTA, VUELVA A INTENTAR! \n")
            time.sleep(2)
    except ValueError:
        print("ERROR: Debe ingresar un valor numérico.")
        time.sleep(2)

