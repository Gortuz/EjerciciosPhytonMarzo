def imprimir(tabla):
    for i in range(len(tabla)):
        print("[",end="")
        for j in range(len(tabla)):
            print("%4s"%tabla[i][j], end="")
        print("  ]")

def tablaSec(n):
    tabla = []
    cont = 0
    for i in range (n):
        tabla.append([])
        for j in range (n):
            cont += 1
            tabla[i] += [cont]
    return tabla

tabla = tablaSec(10)
imprimir(tabla)