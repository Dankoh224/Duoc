sw = 1
while sw == 1:
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    op = int(input("Seleccione una opción: "))
    try:
        if op > 0 and op < 4:
            if op == 1:
                print("Ha seleccionado la opción 1.")
                continu = int(input("Desea salir? 1 = Si 2 = No: "))
                if continu == 1:
                    print("Adios")
                    sw = 0
                if continu == 1:
                    print("Adios")
                    sw = 0
                if continu == 1:
                    print("Adios")
                    sw = 0

