def imprimir(dic):
    for i in dic:
        print("Producto:",i," - $",dic[i])
dic = {}
menu = True
while menu:
    print()
    opc = int(input("Menu\n1.- Agregar Producto\n2.- Facturar\n3.- Salir\n"))
    if opc == 1:
        indice = input("Nombre del producto: ")
        valor = float(input("Valor: "))
        dic[indice] = valor
        imprimir(dic)
    elif opc == 2:
        factura = True
        while factura:
            imprimir(dic)
            print("-----Facturando-----\n1.- Agregar a factura\n2.- Finalizar")
            opf = int(input(""))
            if opf == 1:
                total = 0
                indice = input("\nIngrese producto: ")
                cantidad = int(input("Cantidad: "))
                if dic.get(indice) is None:
                    print("Producto no encontrado")
                else:
                    total += dic.get(indice) * cantidad
                    print("El total es: ",total)
            elif opc == 2:
                print("Saliendo...")
                factura = False
    elif opc == 3:
        print("Saliendo...")
        menu = False
    else:
        print("Elija una opción valida")