dic = {}

menu = True
while menu:
    opc = int(input("Elija una opción\n1.- Agregar\n2.- Salir\n"))
    if opc == 1:
        indice = input("Ingrese el índice: ")
        valor = input("Ingrese el valor: ")
        dic[indice] = valor
        print(dic)
    elif opc == 2:
        print("Saliendo...")
        menu = False
    else:
        print("Elija una opción valida")
