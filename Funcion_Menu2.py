def menu(*args):
    while True:
        i=1
        for arg in args:
            print(i,'.-',arg)
            i+=1
        try:
            opc=int(input('\nIngrese Opción: '))
            if opc>0 and opc<i:
                return(opc)
            else:
                print('Opción Incorrecta - Intente Nuevamente')
        except:
            print('Opción Inválida - Intente Nuevamente')

#Llamada a función menu.
print(menu('Ingreso','Modificación','Eliminación','Consultar','Salir'))
    

