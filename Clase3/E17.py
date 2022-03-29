saldo = 0
opc = 0
while(opc != 3):
    print("-----Opciones-----\n1.- Depósito\n2.- Retiro\n3.- Salir")
    opc = int(input("Opción: "))

    print("Saldo actual:",saldo)
    if opc < 0 or opc > 3:
        print("Opción no valida")
        print()
        continue

    if(opc == 1):
        print("\n--- Deposito ---")
        cantidad = float(input("Ingrese la cantidad a depositar: "))
        saldo += cantidad
        print()
    if(opc == 2):
        print("\n--- Retiro ---")
        cantidad = float(input("Ingrese la cantidad a retirar: "))
        if cantidad > saldo:
            print("Saldo insuficiente")
        else:
            saldo -= cantidad
        print()

    if(opc == 3):
        print("\n--- Salir ---")
        print("Gracias por preferirnos")

    
