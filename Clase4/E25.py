def imprimir(tabla):
    for i in range(len(tabla)):
        print("[",end="")
        for j in range(len(tabla)):
            print("%4s"%tabla[i][j], end="")
        print("   ]")

def llenarVacio(n):
    tabla = []
    for i in range(n):
        tabla.append([])
        for j in range(n):
            tabla[i] += " "
    return tabla

def llenarPatron(tabla, simbolo):
    if len(tabla)%2 != 0:
        for i in range(len(tabla)):
            for j in range(len(tabla)):
                if i == j or i + j == len(tabla)-1 or i == len(tabla)//2 or j == len(tabla)//2:
                    tabla[i][j] = simbolo
        imprimir(tabla)
    else:
        print("La tabla es de tamaño PAR")
tabla = llenarVacio(5)
llenarPatron(tabla, "*")
